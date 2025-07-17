from datetime import datetime

import pytest


@pytest.fixture
def card_numbers():
    return [
        "1234567890123456",  # валидный номер
        "1234-5678-9012-3456",  # с разделителями
        "123456789012345",  # короткий
        "12345678901234567890",  # длинный
    ]


@pytest.fixture
def account_numbers():
    return [
        "40817810000000000000",  # валидный счет
        "4081781000000000000",  # короткий
        "408178100000000000000",  # длинный
    ]


@pytest.fixture
def transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 142264000,
            "state": "EXECUTED",
            "date": "2010-06-04T23:20:05.206878",
            "operationAmount": {
                "amount": "714.00",
                "currency": {"name": "EUR", "code": "EUR"},
            },
            "description": "Перевод с карты на карту",
            "from": "Счет 19708645243227258000",
            "to": "Счет 75651667383060284111",
        },
    ]
