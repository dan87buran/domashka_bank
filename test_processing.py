
from ..processing import filter_by_state, sort_by_date
import pytest


@pytest.mark.parametrize("state,expected", [
    ("EXECUTED", 1),  # Ожидаем 1 элемент
    ("PENDING", 1),  # Ожидаем 1 элемент
    ("CANCELLED", 0)  # Нет элементов с таким состоянием
])
def test_filter_by_state(transactions, state, expected):
    result = filter_by_state(transactions, state)
    assert len(result) == expected


def test_sort_by_date(transactions):
    # Сортировка по убыванию
    sorted_desc = sort_by_date(transactions, ascending=False)
    assert sorted_desc[0]["date"] > sorted_desc[1]["date"]

    # Сортировка по возрастанию
    sorted_asc = sort_by_date(transactions, ascending=True)
    assert sorted_asc[0]["date"] < sorted_asc[1]["date"]

    # Тест на одинаковые даты
    transactions[0]["date"] = transactions[1]["date"]
    sorted_same = sort_by_date(transactions)
    assert sorted_same[0]["date"] == sorted_same[1]["date"]

    # Тест на некорректный формат даты
    transactions[0]["date"] = "некорректная дата"
    with pytest.raises(ValueError):
        sort_by_date(transactions)
