from typing import List, Dict
from datetime import datetime


def filter_by_status(data: List[Dict], status: str) -> List[Dict]:
    """
    Фильтрует операции по статусу

    Args:
        data: Список операций
        status: Статус для фильтрации

    Returns:
        Отфильтрованный список операций
        :rtype: List[Dict]
    """
    return [op for op in data if op.get('status', '').upper() == status.upper()]


def sort_by_date(data: List[Dict], reverse: bool = False) -> List[Dict]:
    """
    Сортирует операции по дате

    Args:
        data: Список операций
        reverse: Флаг обратной сортировки

    Returns:
        Отсортированный список операций
    """

    def get_date(op):
        date_str = op.get('date', '')
        try:
            return datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError:
            return datetime.min

    return sorted(data, key=get_date, reverse=reverse)


def filter_by_currency(data: List[Dict], currency: str = 'RUB') -> List[Dict]:
    """
    Фильтрует операции по валюте

    Args:
        data: Список операций
        currency: Код валюты для фильтрации

    Returns:
        Отфильтрованный список операций
    """
    return [op for op in data if op.get('currency', '').upper() == currency.upper()]