import os
import requests
from typing import Dict, Optional
from dotenv import load_dotenv

load_dotenv()


class Optionalfloat:
    pass


class CurrencyConverter:
    API_URL = "https://api.apilayer.com/exchangerates_data/latest"

    @staticmethod
    def convert_to_rub(transaction: Dict) -> Optionalfloat:
        """Конвертирует сумму транзакции в рубли."""
        if not transaction or 'amount' not in transaction or 'currency' not in transaction:
            return None

        try:
            amount = float(transaction['amount'])
            currency = transaction['currency']

            if currency == 'RUB':
                return amount

            api_key = os.getenv('EXCHANGE_RATE_API_KEY')
            if not api_key:
                raise ValueError("API key not configured")

            response = requests.get(
                CurrencyConverter.API_URL,
                params={'base': currency, 'symbols': 'RUB'},
                headers={'apikey': api_key},
                timeout=10
            )
            response.raise_for_status()

            rate = response.json()['rates']['RUB']
            return round(amount * rate, 2)

        except (ValueError, TypeError, requests.RequestException, KeyError) as e:
            print(f"Conversion error: {e}")
            return None
