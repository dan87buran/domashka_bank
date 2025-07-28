import json
from typing import List, Dict, Union


def load_transactions(file_path: str) -> List[Dict[str, Union[str, float]]]:
    """
    Загружает транзакции из JSON-файла.

    Args:
        file_path: Путь к JSON-файлу с транзакциями

    Returns:
        Список словарей с транзакциями или пустой список при ошибках
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []