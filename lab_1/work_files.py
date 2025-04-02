import json

def load_json(file_name: str) -> dict:
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
