import os
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding as asym_padding
from file_utils import *


def generate_keys(config: dict, key_bits: int) -> None:
    """
    Generates a pair of RSA keys and a symmetric key for encryption.
    The symmetric key is encrypted with the public key and saved to disk.
    
    args:
        config (dict): Configuration dictionary containing paths for saving keys.
        key_bits (int): The length of key.
    """
    try:
        print("Generating RSA key pair and symmetric key...")

        if not (32 <= key_bits <= 448 and key_bits % 8 == 0):
            raise ValueError("Blowfish key length must be between 32-448 bits in 8-bit increments.")

        key_bytes = os.urandom(key_bits // 8)
        save_binary(config["symmetric_key"], key_bytes)

        private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        public_key = private_key.public_key()
        
        save_binary(
            config["public_key"],
            public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo,
            ),
        )
        
        save_binary(
            config["secret_key"],
            private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption(),
            ),
        )

        c_text = public_key.encrypt(
            key_bytes,
            asym_padding.OAEP(
                mgf=asym_padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None,
            ),
        )
        
        save_binary(config["encrypted_symmetric_key"], c_text)

        print("RSA keys and symmetric key generated and saved successfully.")
    
    except ValueError as e:
        raise ValueError(f"Invalid key length: {e}")
    except Exception as e:
        raise RuntimeError(f"Error during key generation: {e}")
