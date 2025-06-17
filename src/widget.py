def mask_account_card(card_info: str) -> str:
    """
    Маскирует номер карты, сохраняя тип платежной системы
    """
    # Разделяем тип и номер карты
    parts = card_info.split(maxsplit=1)
    card_type = parts[0]
    card_number = parts[1].replace(" ", "")  # Удаляем пробелы

    # Маскируем только нужные части номера
    return f"{card_type} {card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def mask_account(account_info: str) -> str:
    """
    Маскирует номер счета
    """
    # Разделяем тип и номер счета
    parts = account_info.split(maxsplit=1)
    account_type = parts[0]
    account_number = parts[1]

    # Маскируем все, кроме последних 4 цифр
    return f"{account_type} **{account_number[-4:]}"


def get_date(date_str: str) -> str:
    """
    Преобразует дату из формата YYYY-MM-DD в DD.MM.YYYY
    """
    # Разделяем дату и время
    date_part = date_str.split('T')[0]

    # Разделяем дату на части
    year, month, day = date_part.split("-")

    # Формируем новый формат
    return f"{day}.{month}.{year}"


