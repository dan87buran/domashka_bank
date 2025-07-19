import pytest
from typing import Union

from src.decorators import log


# Твой декоратор и функция остаются без изменений

# Тестирование

def test_log(capsys):
    @log()
    def get_mask_card_number(card_number: Union[int, str]) -> str:
        """Функция принимает на вход номер карты в виде числа и
        возвращает маску номера по правилу XXXX XX** **** XXXX"""
        if not isinstance(card_number, int) and not isinstance(card_number, str):
            raise TypeError("Неверный формат входного значения")

        if len(str(card_number)) != 16:
            raise ValueError("Неверная длина номера карты")

        return f"{str(card_number)[:4]} {str(card_number)[4:6]}** **** {str(card_number)[12:]}"

    get_mask_card_number(1234)
    capture = capsys.readouterr()
    assert capture.out == "get_mask_card_number error: ValueError. Inputs: (1234,), {}\n"
