from collections import Counter
from work_files import load_json, load_text, save_text
import json


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


def main():
    settings = load_json("settings.json")
    source_text = settings.get("SOURCE_TEXT", "")
    first_key = load_json(settings.get("FIRST_KEY", ""))
    second_key = load_json(settings.get("SECOND_KEY", ""))
    decrypted_text = settings.get("DECRYPTED_TEXT", "")
    try:
        text = load_text(source_text)
        print("Исходный текст: ", text)
        count_freq(text)
        text = replace_text(text, first_key)
        print("\n", "Первая замена: ", text)
        text = replace_text(text, second_key)
        print("\n", "Вторая замена: ", text)
        save_text(text, decrypted_text)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
