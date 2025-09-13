from typing import Dict

import file_reader
from coverage import data

from filters import filter_by_status, sort_by_date, filter_by_currency
from src.bank_operation import process_bank_search


def format_operation(operation: Dict) -> str:
    """
    Форматирует операцию для вывода

    Args:
        operation: Словарь с данными об операции

    Returns:
        Отформатированная строка с информацией об операции
    """
    date = operation.get('date', '')
    description = operation.get('description', '')
    from_account = operation.get('from', '')
    to_account = operation.get('to', '')
    amount = operation.get('amount', '')
    currency = operation.get('currency', '')

    # Маскирование номеров счетов/карт
    if from_account:
        if 'счет' in from_account.lower():
            from_account = f"Счет **{from_account[-4:]}" if len(from_account) >= 4 else from_account
        else:
            parts = from_account.split()
            if len(parts) > 1:
                card_number = parts[-1]
                if len(card_number) >= 16:
                    masked = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
                    from_account = ' '.join(parts[:-1] + [masked])

    if to_account:
        if 'счет' in to_account.lower():
            to_account = f"Счет **{to_account[-4:]}" if len(to_account) >= 4 else to_account

    # Формирование строки
    result = f"{date} {description}\n"
    if from_account:
        result += f"{from_account} -> "
    if to_account:
        result += f"{to_account}\n"
    result += f"Сумма: {amount} {currency}\n"

    return result


def read_xlsx_file():
    pass


def read_csv_file():
    pass


def read_json_file():
    pass


def main():
    """
    Основная функция программы
    """
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    while True:
        print("\nВыберите необходимый пункт меню:")
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла")
        print("4. Выход")

        choice = input("Ваш выбор: ").strip()

        if choice == '4':
            print("До свидания!")
            break

        input("Введите путь к файлу: ").strip()

        try:
            if choice == '1':
                read_json_file()
                print("Для обработки выбран JSON-файл.")
            elif choice == '2':
                read_csv_file()
                print("Для обработки выбран CSV-файл.")
            elif choice == '3':
                read_xlsx_file()
                print("Для обработки выбран XLSX-файл.")
            else:
                print("Неверный выбор. Попробуйте снова.")
                continue

            if not data:
                print("Не удалось загрузить данные или файл пуст.")
                continue

            # Фильтрация по статусу
            while True:
                print("\nВведите статус, по которому необходимо выполнить фильтрацию.")
                print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")

                status = input("Статус: ").strip().upper()

                if status in ['EXECUTED', 'CANCELED', 'PENDING']:
                    filtered_data = filter_by_status( data, status)
                    print(f"Операции отфильтрованы по статусу \"{status}\"")
                    break
                else:
                    print(f"Статус операции \"{status}\" недоступен.")

            if not filtered_data:
                print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
                continue

            # Сортировка по дате
            sort_choice = input("\nОтсортировать операции по дате? (Да/Нет): ").strip().lower()
            if sort_choice in ['да', 'yes', 'y']:
                order_choice = input("Отсортировать по возрастанию или по убыванию? ").strip().lower()
                reverse = order_choice in ['по убыванию', 'убыванию', 'desc', 'reverse']
                filtered_data = sort_by_date(filtered_data, reverse)

            # Фильтрация по валюте
            currency_choice = input("\nВыводить только рублевые транзакции? (Да/Нет): ").strip().lower()
            if currency_choice in ['да', 'yes', 'y']:
                filtered_data = filter_by_currency(filtered_data, 'RUB')

            # Поиск по описанию
            search_choice = input(
                "\nОтфильтровать список транзакций по определенному слову в описании? (Да/Нет): ").strip().lower()
            if search_choice in ['да', 'yes', 'y']:
                search_term = input("Введите слово для поиска: ").strip()
                filtered_data = process_bank_search(filtered_data, search_term)

            # Вывод результатов
            if not filtered_data:
                print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
            else:
                print(f"\nРаспечатываю итоговый список транзакций...")
                print(f"Всего банковских операций в выборке: {len(filtered_data)}\n")

                for operation in filtered_data:
                    print(format_operation(operation))
                    print("-" * 50)

        except Exception as e:
            print(f"Ошибка при обработке файла: {e}")


if __name__ == "__main__":
    main()