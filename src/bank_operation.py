import re
from typing import List, Dict
from collections import Counter


def process_bank_search(data: List[Dict], search: str) -> List[Dict]:
    """
    Фильтрует список банковских операций по строке поиска в описании
    с использованием регулярных выражений

    Args:
        data: Список словарей с данными о банковских операциях
        search: Строка для поиска в описании операций

    Returns:
        Отфильтрованный список операций, содержащих искомую строку
    """
    try:
        pattern = re.compile(search, re.IGNORECASE)
        return [operation for operation in data if pattern.search(operation.get('description', ''))]
    except re.error:
        return []


def process_bank_operations(data: List[Dict], categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество операций в каждой категории

    Args:
        data: Список словарей с данными о банковских операциях
        categories: Список категорий для подсчета

    Returns:
        Словарь с количеством операций по каждой категории
    """
    descriptions = [op.get('description', '') for op in data]
    counter = Counter(descriptions)
    return {category: counter[category] for category in categories if category in counter}