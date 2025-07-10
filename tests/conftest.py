import pytest
from datetime import datetime

@pytest.fixture
def card_numbers():
    return [
        "1234567890123456",  # валидный номер
        "1234-5678-9012-3456",  # с разделителями
        "123456789012345",  # короткий
        "12345678901234567890"  # длинный
    ]

@pytest.fixture
def account_numbers():
    return [
        "40817810000000000000",  # валидный счет
        "4081781000000000000",  # короткий
        "408178100000000000000"  # длинный
    ]

@pytest.fixture
def transactions():
    return [
        {
            "state": "EXECUTED",
            "date": "2023-01-01T12:00:00",
            "amount": 1000
        },
        {
            "state": "PENDING",
            "date": "2023-01-02T12:00:00",
            "amount": 2000
        }
    ]
