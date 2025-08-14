import pytest
from src.read_operation import (
    get_valid_status,
    ask_yes_no,
    ask_sort_order,
    filter_transactions,
    print_transactions,
    print_no_transactions_message,
    Transaction
)

# Тестовые данные
TEST_TRANSACTIONS = [
    {
        'date': '08.12.2019',
        'description': 'Открытие вклада',
        'from': 'Счет 4321',
        'to': '',
        'amount': '40542',
        'currency': 'руб.',
        'status': 'EXECUTED'
    },
    {
        'date': '12.11.2019',
        'description': 'Перевод с карты на карту',
        'from': 'MasterCard 7771 27****3727',
        'to': 'Visa Platinum 1293 38****9203',
        'amount': '130',
        'currency': 'USD',
        'status': 'EXECUTED'
    },
    {
        'date': '03.06.2018',
        'description': 'Перевод со счета на счет',
        'from': 'Счет **2935',
        'to': 'Счет **4321',
        'amount': '8200',
        'currency': 'EUR',
        'status': 'CANCELED'
    }
]


def test_get_valid_status(monkeypatch):
    # Тест корректного ввода
    monkeypatch.setattr('builtins.input', lambda _: 'EXECUTED')
    assert get_valid_status() == 'EXECUTED'

    # Тест некорректного, затем корректного ввода
    inputs = iter(['invalid', 'PENDING'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert get_valid_status() == 'PENDING'


def test_ask_yes_no(monkeypatch):
    # Тест ответа "Да"
    monkeypatch.setattr('builtins.input', lambda _: 'да')
    assert ask_yes_no('Тест?') is True

    # Тест ответа "Нет"
    monkeypatch.setattr('builtins.input', lambda _: 'нет')
    assert ask_yes_no('Тест?') is False

    # Тест некорректного ввода
    inputs = iter(['maybe', 'д'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert ask_yes_no('Тест?') is True


def test_ask_sort_order(monkeypatch):
    # Тест корректного ввода
    monkeypatch.setattr('builtins.input', lambda _: 'по возрастанию')
    assert ask_sort_order() == 'по возрастанию'

    # Тест некорректного ввода
    inputs = iter(['random', 'по убыванию'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert ask_sort_order() == 'по убыванию'


def test_print_transactions(capsys):
    print_transactions(TEST_TRANSACTIONS[:1])
    captured = capsys.readouterr()
    assert '08.12.2019 Открытие вклада' in captured.out
    assert '40542 руб.' in captured.out


def test_print_no_transactions(capsys):
    print_no_transactions_message()
    captured = capsys.readouterr()
    assert 'Не найдено ни одной транзакции' in captured.out


def test_filter_transactions(monkeypatch, capsys):
    # Мокаем все пользовательские вводы
    inputs = iter([
        'EXECUTED',  # Статус
        'да',  # Сортировать?
        'по возрастанию',  # Порядок
        'нет',  # Только рубли?
        'нет'  # Фильтр по слову?
    ])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    filter_transactions(TEST_TRANSACTIONS)
    captured = capsys.readouterr()
    assert 'Операции отфильтрованы по статусу "EXECUTED"' in captured.out
    assert 'Всего банковских операций в выборке: 2' in captured.out