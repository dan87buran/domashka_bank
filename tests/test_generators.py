from src.generators import (card_number_generator, filter_by_currency, start,
                            transaction_descriptions, transactions)


def test_filter_by_currency_USD(transactions):
    usd = filter_by_currency(transactions, "USD")
    result = list(usd)
    assert result == [
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
    ]


def test_filter_by_currency_EUR(transactions):
    eur = filter_by_currency(transactions, "EUR")
    result = list(eur)
    assert result == [
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


def test_filter_by_currency_USDT(transactions):
    usdt = filter_by_currency(transactions, "USDT")
    result = list(usdt)
    assert result == []


def test_transaction_descriptions(transactions):
    descriptions = transaction_descriptions(transactions)
    result = list(descriptions)
    assert result == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
    ]


def test_card_number_generator():
    start = "0000 0000 0000 0001"
    end = "0000 0000 0000 0004"
    numder_card = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
    ]
    result = list(card_number_generator(start, end))
    assert result == numder_card
