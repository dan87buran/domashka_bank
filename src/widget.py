from masks import get_mask_card_number


def mask_account_card(card_info: str) -> str:
    """
    Маскирует номер карты, сохраняя тип платежной системы
    """
    # Разделяю тип и номер карты
    parts = card_info.split(maxsplit=1)
    card_type = parts[0]
    card_number = parts[1].replace(" ", "")  # Удаляю пробелы

    # Применяю маскировку
    return f"{card_type} {get_mask_card_number(card_number)}"


def get_date(date_str: str) -> str:
    """
    Преобразует дату из формата ГГГГ-MM-ДД в ДД.MM.ГГГГ
    """
    # Разделяю дату на части
    year, month, day = date_str.split("-")
    # Формирую новый формат
    return f"{day}.{month}.{year}"

