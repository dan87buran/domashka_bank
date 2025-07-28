import unittest
from unittest.mock import patch
from src.external_api import convert_to_rub


class TestExternalAPI(unittest.TestCase):
    @patch('requests.get')
    def test_convert_usd_to_rub(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {'rates': {'RUB': 75.50}}

        transaction = {'amount': '100', 'currency': 'USD'}
        result = convert_to_rub(transaction)
        self.assertEqual(result, 7550.0)

    def test_convert_rub(self):
        transaction = {'amount': '100', 'currency': 'RUB'}
        result = convert_to_rub(transaction)
        self.assertEqual(result, 100.0)
