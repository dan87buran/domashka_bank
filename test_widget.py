
from widget import mask_account_card, get_date
import pytest
from datetime import datetime


def test_mask_account_card():
    # Проверяем маскирование карты
    assert mask_account_card("1234567890123456") == "1234 56** **** 3456"

    # Проверяем маскирование счета
    assert mask_account_card("40817810000000000000") == "4081781000000000****0000"

    # Проверяем некорректный ввод
    with pytest.raises(ValueError):
        mask_account_card("неверный формат")



        # Тест на некорректную дату
        with pytest.raises(ValueError):
            get_date("2023-02-30T12:00:00")

        # Тест на пустую строку
        with pytest.raises(ValueError):
            get_date("")
