import os
from cryptography.hazmat.primitives.ciphers import Cipher, modes
from cryptography.hazmat.primitives import padding as sym_padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.decrepit.ciphers.algorithms import Blowfish
from cryptography.hazmat.primitives.asymmetric import padding as asym_padding
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from file_utils import *
from symmetric_crypto import pad, unpad

def decrypt_symmetric_key(enc_sym_key_path: str, priv_key_path: str) -> bytes:
    """
    Decrypts the symmetric key using RSA private key.
    
    args:
        enc_sym_key_path (str): Path to the encrypted symmetric key file.
        priv_key_path (str): Path to the RSA private key file.
    
    return:
        dc_text (bytes): The decrypted symmetric key.
    """
    try:
        print("Decrypting symmetric key...")

        enc_sym_key = load_binary(enc_sym_key_path)
        private_key = load_pem_private_key(load_binary(priv_key_path), password=None)
        
        dc_text = private_key.decrypt(enc_sym_key, asym_padding.OAEP(mgf=asym_padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))

        print("Symmetric key decrypted successfully.")
        return dc_text
    except FileNotFoundError:
        raise FileNotFoundError("The specified file(s) not found.")
    except Exception as e:
        raise ValueError(f"Error during symmetric key decryption: {e}")


def encrypt_data(config: dict) -> None:
    """
    Encrypts the data using the decrypted symmetric key and Blowfish encryption.
    
    args:
        config (dict): Configuration dictionary containing paths to input/output files and keys.
    """
    try:
        print("Starting encryption process...")
        
        key = decrypt_symmetric_key(config["encrypted_symmetric_key"], config["secret_key"])
        text = load_text_file(config["initial_file"])
        padded = pad(text.encode("utf-8"), 8)
        iv = os.urandom(8)
        cipher = Cipher(Blowfish(key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        c_text = encryptor.update(padded) + encryptor.finalize()
        save_binary(config["encrypted_file"], iv + c_text)
        print("Data successfully encrypted and saved.")
    
    except Exception as e:
        raise RuntimeError(f"Error during encryption: {e}")


def decrypt_data(config: dict) -> None:
    """
    Decrypts the encrypted data using the decrypted symmetric key and Blowfish decryption.
    
    args:
        config (dict): Configuration dictionary containing paths to input/output files and keys.
    """
    try:
        print("Starting decryption process...")
        key = decrypt_symmetric_key(config["encrypted_symmetric_key"], config["secret_key"])
        data = load_binary(config["encrypted_file"])
        iv, ciphertext = data[:8], data[8:]
        cipher = Cipher(Blowfish(key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        padded_plain = decryptor.update(ciphertext) + decryptor.finalize()
        unpadded = unpad(padded_plain, 8)
        save_text_file(config["decrypted_file"], unpadded.decode("utf-8"))
        print("Data successfully decrypted and saved.")
    
    except Exception as e:
        raise RuntimeError(f"Error during decryption: {e}")
