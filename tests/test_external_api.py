import pytest
from unittest.mock import patch, Mock

from src.external_api import CurrencyConverter


def test_convert_rub_without_api_call():
    """Тест для транзакций в рублях"""
    assert CurrencyConverter.convert_to_rub({
        'amount': '100',
        'currency': 'RUB'
    }) == 100.0


@patch.dict('os.environ', {'EXCHANGE_RATE_API_KEY': 'test_key'})
@patch('src.external_api.requests.get')
def test_convert_foreign_currency(mock_get):
    """Тест для конвертации иностранной валюты"""
    # Настраиваем мок
    mock_response = Mock()
    mock_response.json.return_value = {'rates': {'RUB': 75.0}}
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    # Вызываем тестируемую функцию
    result = CurrencyConverter.convert_to_rub({
        'amount': '10',
        'currency': 'USD'
    })

    # Проверяем результаты
    assert result == 750.0
    mock_get.assert_called_once_with(
        CurrencyConverter.API_URL,
        params={'base': 'USD', 'symbols': 'RUB'},
        headers={'apikey': 'test_key'},
        timeout=10
    )


def test_convert_without_api_key():
    """Тест без API ключа"""
    with patch.dict('os.environ', {}, clear=True):
        result = CurrencyConverter.convert_to_rub({
            'amount': '10',
            'currency': 'USD'
        })
        assert result is None


def test_invalid_transaction():
    """Тест для невалидных данных"""
    assert CurrencyConverter.convert_to_rub({}) is None
    assert CurrencyConverter.convert_to_rub({'amount': '10'}) is None
    assert CurrencyConverter.convert_to_rub({'currency': 'USD'}) is None
