from typing import List, Dict
from datetime import datetime


def filter_by_state(transactions: List[Dict], state: str) -> List[Dict]:
    """
    Фильтрует транзакции по указанному состоянию.

    Args:
        transactions: Список словарей с транзакциями
        state: Состояние для фильтрации

    Returns:
        Отфильтрованный список транзакций
    """
    return [t for t in transactions if t.get('state') == state]


def sort_by_date(transactions: List[Dict], descending: bool = True) -> List[Dict]:
    """
    Сортирует транзакции по дате.

    Args:
        transactions: Список словарей с транзакциями
        descending: Флаг сортировки по убыванию (по умолчанию True)

    Returns:
        Отсортированный список транзакций
    """
    def get_date(transaction):
        try:
            return datetime.fromisoformat(transaction['date'])
        except (ValueError, KeyError):
            raise ValueError("Некорректный формат даты")

    try:
        return sorted(
            transactions,
            key=get_date,
            reverse=descending
        )
    except ValueError as e:
        raise ValueError(f"Ошибка при сортировке: {e}")