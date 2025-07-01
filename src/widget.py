from masks import get_mask_card_number, get_mask_account_number


def mask_account_card(info: str) -> str:
    if info.startswith("Счет "):
        # Работаем со счётом
        number = info[5:]
        masked = get_mask_account_number(number)
        return f"Счет {masked}"
    else:
        # Работаем с картой
        *name_parts, number = info.split()
        card_name = ' '.join(name_parts)
        masked = get_mask_card_number(number)
        return f"{card_name} {masked}"


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
