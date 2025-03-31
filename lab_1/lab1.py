import json

def load_key(file_name: str) -> dict:
    """
    Загружает ключ из JSON файла.
    
    args:
        file_name (str): Название файла с ключом.
    
    return: 
        dict: Ключ в виде словаря.
    """
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            return json.load(file)
        
    except Exception as e:
        print(e)


def load_text(file_name: str) -> str:
    """
    Загружает текст из файла.
    
    args:
        file_name(str): Название файла с текстом.
    
    return: 
        str: Содержимое файла.
    """
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            return file.read()
        
    except Exception as e:
        print(e)


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


def save_text(text, output_file : str) -> str:
    """
    Сохраняет текст в файл.

    args: 
        text(str): Текст, который нужно сохранить.
        output_file: Название файла, в который нужно сохранить текст.
    """
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(text)
    
    except Exception as e:
        print(e)


def main():
    key_file = 'key.json'
    source_file = 'source_text.txt'
    changed_file = 'changed_text.txt'
    decrypted_file = 'decrypted_text.txt'

    try:
        key = load_key(key_file)
        text = load_text(source_file)
        changed_text = change_text(text.upper(), key)
        decrypted_text = decrypt_text(changed_text.upper(), key)
        save_text(changed_text, changed_file)
        save_text(decrypted_text, decrypted_file)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
