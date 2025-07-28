import os
import requests
from typing import Dict, Optional
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('EXCHANGE_RATE_API_KEY')
BASE_URL = "https://api.apilayer.com/exchangerates_data/latest"


def convert_to_rub(transaction: Dict[str, str]) -> Optional[float]:
    """
    Конвертирует сумму транзакции в рубли.

    Args:
        transaction: Словарь с данными о транзакции

    Returns:
        Сумма в рублях (float) или None при ошибках
    """
    if not transaction.get('amount'):
        return None

    amount = float(transaction['amount'])
    currency = transaction.get('currency', 'RUB').upper()

    if currency == 'RUB':
        return amount

    if currency not in ('USD', 'EUR'):
        return None

    try:
        response = requests.get(
            BASE_URL,
            params={'base': currency, 'symbols': 'RUB'},
            headers={'apikey': API_KEY},
            timeout=10
        )
        response.raise_for_status()
        rate = response.json()['rates']['RUB']
        return round(amount * rate, 2)
    except (requests.RequestException, KeyError):
        return None
