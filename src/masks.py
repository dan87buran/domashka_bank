def get_mask_card_number(number_card: str) -> str:
    """
    Маскирует номер карты, оставляя видимыми только первые 4 и последние 4 цифры.

    Args:
        number_card (str): Номер карты с пробелами или без

    Returns:
        str: Замаскированный номер карты
    """
    # Удаляю все пробелы
    number_card_1 = number_card.replace(" ", "")
    if len(number_card_1) != 16:
        raise ValueError('не ровняется 16')
    # Разбиваю номер на группы по 4 цифры
    # '40811234112300000000'
    number_slic_1, nuber_slic_2 = number_card_1[0:6], number_card_1[-4:]

    star = "*" * (len(number_card_1) -10)
    number_card_1 = f"{number_slic_1}{star}{nuber_slic_2}"
    mask_card_list = " ".join(
        number_card_1[i : i + 4] for i in range(0, len(number_card_1), 4)
    )

    return mask_card_list


def get_mask_account_number(account_number: str) -> str:
    """
    Маскирует номер счета, оставляя видимыми только последние 4 цифры.

    Args:
        account_number (str): Номер счета

    Returns:
        str: Замаскированный номер счета
    """
    if len(account_number) != 20:
        raise ValueError ('количество символов не равно 20')
    return "**" + account_number[-4:]
