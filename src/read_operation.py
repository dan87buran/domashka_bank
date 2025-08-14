from dis import name
from typing import List, Dict, Literal, Optional
from datetime import datetime

# Типы данных
Status = Literal['EXECUTED', 'CANCELED', 'PENDING']
SortOrder = Literal['по возрастанию', 'по убыванию']
Transaction = Dict[str, str]


def get_valid_status() -> Status:
    """Запрашивает у пользователя валидный статус"""
    valid_statuses: List[Status] = ['EXECUTED', 'CANCELED', 'PENDING']
    while True:
        status = input('Введите статус, по которому необходимо выполнить фильтрацию.\n'
                       'Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n').upper()
        if status in valid_statuses:
            return status
        print(f'Статус операции "{status}" недоступен.')


def ask_yes_no(question: str) -> bool:
    """Задает вопрос с ответом Да/Нет и возвращает булево значение"""
    while True:
        answer = input(f'{question} Да/Нет\n').lower()
        if answer in ('да', 'д'):
            return True
        elif answer in ('нет', 'н'):
            return False
        print('Пожалуйста, ответьте "Да" или "Нет"')


def ask_sort_order() -> SortOrder:
    """Запрашивает порядок сортировки"""
    while True:
        order = input('Отсортировать по возрастанию или по убыванию?\n').lower()
        if order in ('по возрастанию', 'по убыванию'):
            return order
        print('Пожалуйста, укажите "по возрастанию" или "по убыванию"')


def filter_transactions(transactions: List[Transaction]) -> None:
    """Основная функция для фильтрации транзакций"""
    # Шаг 1: Фильтрация по статусу
    status = get_valid_status()
    filtered = [t for t in transactions if t['status'] == status]
    print(f'Операции отфильтрованы по статусу "{status}"')

    if not filtered:
        print_no_transactions_message()
        return

    # Шаг 2: Сортировка по дате
    if ask_yes_no('Отсортировать операции по дате?'):
        order = ask_sort_order()
        filtered.sort(
            key=lambda t: datetime.strptime(t['date'], '%d.%m.%Y'),
            reverse=(order == 'по убыванию')
        )

    # Шаг 3: Фильтрация по валюте
    if ask_yes_no('Выводить только рублевые транзакции?'):
        filtered = [t for t in filtered if t['currency'] == 'руб.']

    # Шаг 4: Фильтрация по ключевому слову
    if ask_yes_no('Отфильтровать список транзакций по определенному слову в описании?'):
        keyword = input('Введите слово для поиска в описании: ').lower()
        filtered = [t for t in filtered if keyword in t['description'].lower()]

    # Вывод результатов
    if not filtered:
        print_no_transactions_message()
    else:
        print_transactions(filtered)


def print_transactions(transactions: List[Transaction]) -> None:
    """Выводит список транзакций"""
    print('Распечатываю итоговый список транзакций...\n')
    print(f'Всего банковских операций в выборке: {len(transactions)}\n')

    for t in transactions:
        print(f"{t['date']} {t['description']}")
        if t['from']:
            print(f"{t['from']} -> {t['to']}" if t['to'] else t['from'])
        print(f"Сумма: {t['amount']} {t['currency']}\n")


def print_no_transactions_message() -> None:
    """Выводит сообщение об отсутствии транзакций"""
    print('Не найдено ни одной транзакции, подходящей под ваши условия фильтрации')


if name == '__main__':
    # Пример данных для демонстрации
    sample_transactions = [
        {
            'date': '08.12.2019',
            'description': 'Открытие вклада',
            'from': 'Счет 4321',
            'to': '',
            'amount': '40542',
            'currency': 'руб.',
            'status': 'EXECUTED'
        },
        # ... другие транзакции
    ]
    filter_transactions(sample_transactions)