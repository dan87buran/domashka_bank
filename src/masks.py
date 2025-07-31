from src.log_config import setup_logger

logger = setup_logger('masks')




def get_mask_card_number(number_card: str) -> str:
    """
    Маскирует номер карты с логированием.
    """
    try:
        logger.debug(f"Попытка маскировки карты: {number_card}")

        number_card_1 = number_card.replace(" ", "")
        if len(number_card_1) != 16:
            logger.error(f"Некорректная длина номера карты: {number_card}")
            raise ValueError('не ровняется 16')

        number_slic_1, nuber_slic_2 = number_card_1[0:6], number_card_1[-4:]
        star = "*" * (len(number_card_1) - 10)
        number_card_1 = f"{number_slic_1}{star}{nuber_slic_2}"
        mask_card_list = " ".join(
            number_card_1[i:i + 4] for i in range(0, len(number_card_1), 4)
        )

        logger.info(f"Успешная маскировка карты: {number_card} -> {mask_card_list}")
        return mask_card_list

    except Exception as e:
        logger.error(f"Ошибка маскировки карты: {e}", exc_info=True)
        raise


def get_mask_account_number(account_number: str) -> str:
    """
    Маскирует номер счета с логированием.
    """
    try:
        logger.debug(f"Попытка маскировки счета: {account_number}")

        if len(account_number) != 20:
            logger.error(f"Некорректная длина номера счета: {account_number}")
            raise ValueError('количество символов не равно 20')

        masked = "**" + account_number[-4:]
        logger.info(f"Успешная маскировка счета: {account_number} -> {masked}")
        return masked

    except Exception as e:
        logger.error(f"Ошибка маскировки счета: {e}", exc_info=True)
        raise