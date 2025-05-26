import json

def load_config(path: str) -> dict:
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def load_text_file(path: str) -> str:
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def save_text_file(path, content: str) -> None:
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)


def load_binary(path: str) -> bytes:
    with open(path, 'rb') as f:
        return f.read()


def save_binary(path, content: str) -> None:
    with open(path, 'wb') as f:
        f.write(content)
