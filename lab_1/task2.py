from collections import Counter
from constants import *
import json


def read_file(file_name: str) -> str:
    """
    Считывает набор символов из исходного файла.

    args:
        file_name(str): Название файла, из которого нужно прочитать набор символов.
        
    return:
        str: Считанный набор символов.
    """
    with open(file_name, 'r', encoding='utf-8') as file:
        return file.read()


def count_freq(text: str) -> dict:
    """
    Вычисляет частоту появления букв в тексте и записывает данные в JSON файл.

    args:
        text(str): Текст, для которого нужно вычислить частоту.

    return:
        dict: Записанные данные о частоте появления букв в JSON файле.
    """
    freq = Counter(text)
    freq_index = {}
    for char, count in freq.items():
            freq_index[char] = count / sum(freq.values())
                          
    with open('freq_index.json', 'w', encoding='utf-8') as json_file:
        json.dump(freq_index, json_file, ensure_ascii=False, indent=2)


def replace_text(text: str, key: dict) -> str:
    """
    Заменяет символы в тексте с помощью ключа шифрования.

    args:
        text(str): Текст, в котором нужно заменить символы.
        key(dict): Ключ шифрования.

    return:
        text(str): Текст с заменёнными символами.
    """
    for old, new in key.items():
        text = text.replace(old, new)
    return text


def save_text(file_name, text: str) -> str:
    """
    Записывает текст, полученный с помощью замены символов в файл.

    args:
        file_name(str): Название файла, куда будет сохранён текст.
        text(str): Текст, который нужно записать.

    return:
        str: Записанный текст в файле.
    """
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(text)


def main():
    try:
        text = read_file(SOURCE_TEXT)
        print("Исходный текст: ", text)
        count_freq(text)
        text = replace_text(text, FIRST_KEY)
        print("\n", "Первая замена: ", text)
        text = replace_text(text, SECOND_KEY)
        print("\n", "Вторая замена: ", text)
        save_text(DECRYPTED_TEXT, text)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
