import os
from cryptography.hazmat.primitives.ciphers import Cipher, modes
from cryptography.hazmat.primitives import padding as sym_padding
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.decrepit.ciphers import algorithms
from cryptography.hazmat.primitives.asymmetric import padding as asym_padding, rsa
from cryptography.hazmat.primitives import hashes

from file_utils import *


def decrypt_symmetric_key(enc_sym_key_path, priv_key_path: str) -> bytes:
    enc_sym_key = load_binary(enc_sym_key_path)
    private_key = load_pem_private_key(load_binary(priv_key_path), password=None)
    dc_text = private_key.decrypt(enc_sym_key, asym_padding.OAEP(mgf=asym_padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
    return dc_text


def encrypt_data(config: dict) -> None:
    key = decrypt_symmetric_key(config["encrypted_symmetric_key"], config["secret_key"])
    text = load_text_file(config["initial_file"])
    padded = pad(text.encode("utf-8"), 8)

    iv = os.urandom(8)
    cipher = Cipher(algorithms.Blowfish(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    c_text = encryptor.update(padded) + encryptor.finalize()

    save_binary(config["encrypted_file"], iv + c_text)


def decrypt_data(config: dict) -> None:
    key = decrypt_symmetric_key(config["encrypted_symmetric_key"], config["secret_key"])
    data = load_binary(config["encrypted_file"])
    iv, ciphertext = data[:8], data[8:]

    cipher = Cipher(algorithms.Blowfish(key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    padded_plain = decryptor.update(ciphertext) + decryptor.finalize()

    unpadded = unpad(padded_plain, 8)
    save_text_file(config["decrypted_file"], unpadded.decode("utf-8"))


def pad(data: bytes, block_size: int = 8) -> bytes:
    padder = sym_padding.ANSIX923(block_size * 8).padder()
    padded_text = padder.update(data) + padder.finalize()
    return padded_text


def unpad(data: bytes, block_size: int = 8) -> bytes:
    unpadder = sym_padding.ANSIX923(block_size * 8).unpadder()
    unpadded_dc_text = unpadder.update(data) + unpadder.finalize()
    return unpadded_dc_text
