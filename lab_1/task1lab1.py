from work_files import load_json, load_text, save_text
import json


def change_text(text: str, key: dict) -> str:
    """
    Шифрует текст с помощью ключа из JSON файла.

    args:
        text (str): Исходный текст.
        key (dict): Ключ в виде словаря.
    
    return: 
        str: Зашифрованный текст.
    """
    return ''.join(key.get(char, char) for char in text)


def decrypt_text(text: str, key: dict) -> str: 
    """
    Дешифрует текст с помощью ключа.
    
    args:
        text (str): Зашифрованный текст.
        key (dict): В виде словаря.

    return: 
        str: Дешифрованный текст.
    """
    reverse_key = {second_char: first_char for first_char, second_char in key.items()}
    return ''.join(reverse_key.get(char, char) for char in text)


def main():
    settings = load_json("../settings.json")
    key_file = settings.get("KEY_FILE", "")
    source_file = settings.get("SOURCE_FILE", "")
    changed_file = settings.get("CHANGED_FILE", "")
    decrypted_file = settings.get("DECRYPTED_FILE", "")
    try:
        key = load_json(key_file)
        text = load_text(source_file)
        changed_text = change_text(text.upper(), key)
        decrypted_text = decrypt_text(changed_text.upper(), key)
        save_text(changed_text, changed_file)
        save_text(decrypted_text, decrypted_file)
    except Exception as e:
        print(e)
