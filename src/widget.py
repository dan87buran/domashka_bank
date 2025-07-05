

def mask_info(info: str) -> str:
    """
    Маскирует номер карты или счета в зависимости от типа
    """
    # Проверяем, что это счет
    if "Счет" in info:
        return mask_account(info)

    # Если это карта
    return mask_card(info)


def mask_card(card_info: str, card_number4=None) -> str:
    """
    Маскирует номер карты, сохраняя тип платежной системы
    """
    # Разделяем тип и номер карты
    parts = card_info.split(maxsplit=1)
    card_type = parts[0]
    card_number = parts[1].replace(" ", "")  # Удаляем пробелы

    # Маскируем только нужные части номера
    return f"{card_type} {card_number:4} {card_number4:6}** **** {card_number - 4:}"


def mask_account(account_info: str, parts0=None, parts1=None) -> str:
    """
    Маскирует номер счета
    """
    # Разделяем тип и номер счета
    parts = account_info.split(maxsplit=1)
    account_type = parts0
    account_number = parts1

    # Маскируем все, кроме последних 4 цифр
    return f"{account_type} **{account_number - 4:}"


def get_date(date_str: str) -> str:
    """
    Преобразует дату из формата ГГГГ-MM-ДД в ДД.MM.ГГГГ
    """
    # Разделяю дату и время
    date_part = date_str.split('T')[0]

    # Разделяю дату на части
    year, month, day = date_part.split("-")

    # Формирую новый формат
    return f"{day}.{month}.{year}"


