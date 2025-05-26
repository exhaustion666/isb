import json
import os

def load_config(path: str) -> dict:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Configuration file not found at {path}.")
    except json.JSONDecodeError:
        raise ValueError(f"Error decoding JSON in file {path}. Check the format.")
    except Exception as e:
        raise RuntimeError(f"Error loading configuration: {e}")


def load_text_file(path: str) -> str:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Text file not found at {path}.")
    except Exception as e:
        raise RuntimeError(f"Error reading text file {path}: {e}")


def save_text_file(path, content: str) -> None:
    try:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
    except Exception as e:
        raise RuntimeError(f"Error saving text file {path}: {e}")


def load_binary(path: str) -> bytes:
    try:
        with open(path, 'rb') as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Binary file not found at {path}.")
    except Exception as e:
        raise RuntimeError(f"Error reading binary file {path}: {e}")


def save_binary(path, content: bytes) -> None:
    try:
        with open(path, 'wb') as f:
            f.write(content)
    except Exception as e:
        raise RuntimeError(f"Error saving binary file {path}: {e}")


def save_encrypted_file(path: str, content: bytes) -> None:
    try:
        with open(path, 'wb') as f:
            f.write(content)
    except Exception as e:
        raise RuntimeError(f"Error saving encrypted file {path}: {e}")


def save_decrypted_file(path: str, content: str) -> None:
    try:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
    except Exception as e:
        raise RuntimeError(f"Error saving decrypted file {path}: {e}")
