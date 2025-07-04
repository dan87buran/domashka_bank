def get_mask_card_number(number_card: str, card=None) -> str:
    """
    Маскирует номер карты, оставляя видимыми только первые 4 и последние 4 цифры.

    Args:
        number_card (str): Номер карты с пробелами или без

    Returns:
        str: Замаскированный номер карты
    """
    # Удаляю все пробелы
    number_card_1 = number_
    card.replace(" ", "")

    # Разбиваю номер на группы по 4 цифры
    mask_card_list = " ".join(
        number_card_1[i : i + 4] for i in range(0, len(number_card_1), 4)
    )

    # Преобразую строку в список
    card_list = list(mask_card_list)

    # Маскирую цифры с 5-й по 14-ю (считая с 1)
    for i in range(len(card_list)):
        if 4 <= i <= 13 and card_list[i] != " ":
            card_list[i] = "*"

    # Собираю результат обратно в строку
    masked_number = "".join(card_list)
    return masked_number


def get_mask_account_number(account_number: str) -> str:
    """
    Маскирует номер счета, оставляя видимыми только последние 4 цифры.

    Args:
        account_number (str): Номер счета

    Returns:
        str: Замаскированный номер счета
    """
    return "*" * (len(account_number) - 4) + account_number[-4:]


def get_mask():
    return None


def get_mask_account():
    return None