import pytest
from src.filters import filter_by_status, sort_by_date, filter_by_currency


def test_filter_by_status():
    test_data = [
        {'status': 'EXECUTED', 'amount': 1000},
        {'status': 'CANCELED', 'amount': 5000},
        {'status': 'PENDING', 'amount': 30000}
    ]

    result = filter_by_status(test_data, 'EXECUTED')
    assert len(result) == 1
    assert result[0]['status'] == 'EXECUTED'


def test_sort_by_date():
    test_data = [
        {'date': '2023-01-15', 'amount': 1000},
        {'date': '2023-03-20', 'amount': 5000},
        {'date': '2023-02-10', 'amount': 30000}
    ]

    result = sort_by_date(test_data)
    assert result[0]['date'] == '2023-01-15'
    assert result[1]['date'] == '2023-02-10'
    assert result[2]['date'] == '2023-03-20'


def test_filter_by_currency():
    test_data = [
        {'currency': 'RUB', 'amount': 1000},
        {'currency': 'USD', 'amount': 5000},
        {'currency': 'RUB', 'amount': 30000}
    ]

    result = filter_by_currency(test_data, 'RUB')
    assert len(result) == 2
    assert all(op['currency'] == 'RUB' for op in result)