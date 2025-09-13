import pytest
import src.bank_operation

from src.bank_operation import process_bank_search, process_bank_operations


def test_process_bank_search():
    test_data = [
        {'description': 'Покупка продуктов', 'amount': 1000},
        {'description': 'Оплата коммунальных услуг', 'amount': 5000},
        {'description': 'Зарплата', 'amount': 30000}
    ]

    result = process_bank_search(test_data, 'продукт')
    assert len(result) == 1
    assert result[0]['description'] == 'Покупка продуктов'


def test_process_bank_operations(process_bank_operation=None):
    test_data = [
        {'description': 'Покупка продуктов', 'amount': 1000},
        {'description': 'Оплата коммунальных услуг', 'amount': 5000},
        {'description': 'Покупка продуктов', 'amount': 2000},
        {'description': 'Зарплата', 'amount': 30000}
    ]

    categories = ['Покупка продуктов', 'Зарплата']
    result = process_bank_operations(test_data, categories)

    assert result['Покупка продуктов'] == 2
    assert result['Зарплата'] == 1
    assert 'Оплата коммунальных услуг' not in result