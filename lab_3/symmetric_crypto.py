import os
from cryptography.hazmat.primitives.ciphers import Cipher, modes
from cryptography.hazmat.primitives import padding as sym_padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import algorithms


def encrypt_data(key: bytes, input_text: str) -> bytes:
    """
    Encrypts the input text using Blowfish symmetric encryption.
    
    args:
        key (bytes): The symmetric key used for encryption.
        input_text (str): The plaintext data to be encrypted.
    
    returns:
        iv + c_text (bytes): The encrypted data.
    """
    try:
        print("Starting data encryption...")
      
        padded = pad(input_text.encode("utf-8"), 8)
        iv = os.urandom(8)
        cipher = Cipher(algorithms.Blowfish(key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        c_text = encryptor.update(padded) + encryptor.finalize()
        
        print("Data successfully encrypted.")
        return iv + c_text
    except Exception as e:
        raise RuntimeError(f"Error encrypting data: {e}")

def decrypt_data(key: bytes, data: bytes) -> str:
    """
    Decrypts the encrypted data using Blowfish symmetric decryption.
    
    args:
        key (bytes): The symmetric key used for decryption.
        data (bytes): The encrypted data (including IV).
    
    return:
        unpadded (str): The decrypted plaintext.
    """
    try:
        print("Starting data decryption...")
        
        iv, ciphertext = data[:8], data[8:]
        cipher = Cipher(algorithms.Blowfish(key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        padded_plain = decryptor.update(ciphertext) + decryptor.finalize()
        unpadded = unpad(padded_plain, 8)
        
        print("Data successfully decrypted.")
        return unpadded.decode("utf-8")
    except Exception as e:
        raise RuntimeError(f"Error decrypting data: {e}")

def pad(data: bytes, block_size: int = 8) -> bytes:
    """
    Pads the input data to ensure it fits the block size using ANSIX923 padding.
    
    args:
        data (bytes): The input data to be padded.
        block_size (int): The block size.
    
    return:
        padded_text (bytes): The padded data.
    """
    try:
        print("Padding data...")
        padder = sym_padding.ANSIX923(block_size * 8).padder()
        padded_text = padder.update(data) + padder.finalize()
        print("Padding applied successfully.")
        return padded_text
    except Exception as e:
        raise RuntimeError(f"Error padding data: {e}")

def unpad(data: bytes, block_size: int = 8) -> bytes:
    """
    Removes padding from the input data.
    
    args:
        data (bytes): The padded data to be unpadded.
        block_size (int): The block size.
    
    return:
        unpadded_dc_text (bytes): The unpadded data.
    """
    try:
        print("Removing padding from data...")
        unpadder = sym_padding.ANSIX923(block_size * 8).unpadder()
        unpadded_dc_text = unpadder.update(data) + unpadder.finalize()
        print("Padding removed successfully.")
        return unpadded_dc_text
    except Exception as e:
        raise RuntimeError(f"Error unpadding data: {e}")
