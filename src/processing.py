from typing import List, Dict
from datetime import datetime

def filter_by_state(operations: List[Dict[str, str]], state: str = 'EXECUTED') -> List[Dict[str, str]]:
    """
    Фильтрует список операций по статусу state

    :param operations: список словарей с операциями
    :param state: значение состояния для фильтрации (по умолчанию 'EXECUTED')
    :return: отфильтрованный список операций
    """
    return [
        operation
        for operation in operations
        if operation.get('state') == state
    ]

def sort_by_date(operations: List[Dict[str, str]], descending: bool = True) -> List[Dict[str, str]]:
    """
    Сортирует список операций по дате

    :param operations: список словарей с операциями
    :param descending: порядок сортировки (True - убывание, False - возрастание)
    :return: отсортированный список операций
    """
    return sorted(
        operations,
        key=lambda x: datetime.fromisoformat(x['date'].replace('T', ' ')),
        reverse=descending)
