# file_utils.py
import json
import os

def load_config(path: str) -> dict:
    """
    Loads a JSON configuration file.
    
    args:
        path (str): The path to the configuration file.
    return:
        config (dict): The loaded configuration as a dictionary.
    """
    try:
        print(f"Loading configuration file: {path}...")
        with open(path, 'r', encoding='utf-8') as f:
            config = json.load(f)
        print("Configuration loaded successfully.")
        return config
    except FileNotFoundError:
        raise FileNotFoundError(f"Configuration file not found at {path}.")
    except json.JSONDecodeError:
        raise ValueError(f"Error decoding JSON in file {path}. Check the format.")
    except Exception as e:
        raise RuntimeError(f"Error loading configuration: {e}")


def load_text_file(path: str) -> str:
    """
    Loads a text file and returns its content as a string.
    
    args:
        path (str): The path to the text file.
    return:
        content (str): The content of the text file.
    """
    try:
        print(f"Reading text file: {path}...")
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        print(f"File {path} read successfully.")
        return content
    except FileNotFoundError:
        raise FileNotFoundError(f"Text file not found at {path}.")
    except Exception as e:
        raise RuntimeError(f"Error reading text file {path}: {e}")


def save_text_file(path, content: str) -> None:
    """
    Saves content to a text file.
    
    args:
        path (str): The path where the content will be saved.
        content (str): The content to be saved.
    """
    try:
        print(f"Saving text to file: {path}...")
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"File {path} saved successfully.")
    except Exception as e:
        raise RuntimeError(f"Error saving text file {path}: {e}")


def load_binary(path: str) -> bytes:
    """
    Loads a binary file and returns its content.
    
    args:
        path (str): The path to the binary file.
    
    returns:
        content (bytes): The content of the binary file.
    """
    try:
        print(f"Reading binary file: {path}...")
        with open(path, 'rb') as f:
            content = f.read()
        print(f"File {path} read successfully.")
        return content
    except FileNotFoundError:
        raise FileNotFoundError(f"Binary file not found at {path}.")
    except Exception as e:
        raise RuntimeError(f"Error reading binary file {path}: {e}")


def save_binary(path, content: bytes) -> None:
    """
    Saves binary content to a file.
    
    args:
        path (str): The path where the binary content will be saved.
        content (bytes): The binary content to be saved.
    """
    try:
        print(f"Saving binary data to file: {path}...")
        with open(path, 'wb') as f:
            f.write(content)
        print(f"File {path} saved successfully.")
    except Exception as e:
        raise RuntimeError(f"Error saving binary file {path}: {e}")


def save_encrypted_file(path: str, content: bytes) -> None:
    """
    Saves an encrypted file.
    
    args:
        path (str): The path where the encrypted file will be saved.
        content (bytes): The encrypted content to be saved.
    """
    try:
        print(f"Saving encrypted file: {path}...")
        with open(path, 'wb') as f:
            f.write(content)
        print(f"Encrypted file {path} saved successfully.")
    except Exception as e:
        raise RuntimeError(f"Error saving encrypted file {path}: {e}")


def save_decrypted_file(path: str, content: str) -> None:
    """
    Saves a decrypted file.
    
    args:
        path (str): The path where the decrypted file will be saved.
        content (str): The decrypted content to be saved.
    """
    try:
        print(f"Saving decrypted file: {path}...")
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Decrypted file {path} saved successfully.")
    except Exception as e:
        raise RuntimeError(f"Error saving decrypted file {path}: {e}")
