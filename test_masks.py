
from masks import get_mask_card_number, get_mask_account  # Исправлено
import pytest


def test_get_mask_card_number(card_numbers):
    # Проверяем базовый случай
    assert get_mask_card_number(card_numbers[0]) == "1234 56** **** 3456"

    # Проверяем случай с разделителями
    assert get_mask_card_number(card_numbers[1]) == "1234 56** **** 3456"

    # Проверяем короткую строку
    with pytest.raises(ValueError):
        get_mask_card_number(card_numbers[2])

    # Проверяем длинную строку
    with pytest.raises(ValueError):
        get_mask_card_number(card_numbers[3])


@pytest.mark.parametrize("account", [
    "40817810000000000000",  # валидный
    "4081781000000000000",  # короткий
    "408178100000000000000"  # длинный
])
def test_get_mask_account(account):
    if len(account) == 20:
        assert get_mask_account(account) == "4081781000000000****0000"
    else:
        with pytest.raises(ValueError):
            get_mask_account(account)
