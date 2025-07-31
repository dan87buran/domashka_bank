import unittest
from dis import name
from unittest.mock import patch


def convert_to_rub(transaction):
    """Простая конвертация в рубли"""
    try:
        op_amount = transaction['operationAmount']
        amount = float(op_amount['amount'])
        currency = op_amount['currency']['code'].upper()

        if currency == 'RUB':
            return amount

        if currency in ('USD', 'EUR'):
            # Здесь будет запрос к API (упрощенно)
            rate = get_exchange_rate(currency)
            return round(amount * rate, 2)

    except (KeyError, ValueError, TypeError):
        pass
    return None


def get_exchange_rate(currency):
    """Мок функции для получения курса"""
    rates = {'USD': 75.50, 'EUR': 85.00}
    return rates.get(currency, 1.0)


class TestConvertToRub(unittest.TestCase):
    def test_convert_usd(self):
        trans = {
            'operationAmount': {
                'amount': '100',
                'currency': {'code': 'USD'}
            }
        }
        self.assertEqual(convert_to_rub(trans), 7550.0)

    def test_convert_rub(self):
        trans = {
            'operationAmount': {
                'amount': '100',
                'currency': {'code': 'RUB'}
            }
        }
        self.assertEqual(convert_to_rub(trans), 100.0)

    def test_invalid_data(self):
        self.assertIsNone(convert_to_rub({}))
        self.assertIsNone(convert_to_rub({'operationAmount': {}}))
        self.assertIsNone(convert_to_rub({'operationAmount': {'amount': 'abc'}}))


if name == '__main__':
    unittest.main()