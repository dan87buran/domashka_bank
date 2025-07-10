

import pytest
from datetime import datetime

from src.widget import mask_account_card, get_date


def test_mask_account_card():
    # Проверяем маскирование карты
    assert mask_account_card("card 1234567890123456") == "card 1234 56** **** 3456"

    # Проверяем маскирование счета
    assert mask_account_card("Счет 40817810000000000000") == "Счет **0000"

    # Проверяем некорректный ввод
    with pytest.raises(ValueError):
        mask_account_card("неверный формат")

    assert get_date("2023-02-30T12:00:00") == "30.02.2023"

    # Тест на некорректную дату
    with pytest.raises(ValueError):
        get_date("2023-0230T12:00:00")

    # Тест на пустую строку
    with pytest.raises(ValueError):
        get_date("")

