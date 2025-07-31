import os
import requests
from typing import Dict, Optional
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('EXCHANGE_RATE_API_KEY')
BASE_URL = "https://api.apilayer.com/exchangerates_data/latest"


def convert_to_rub(transaction: Dict) -> Optional[float]:
    """
    Конвертирует сумму транзакции в рубли.
    Новая версия с учётом вложенной структуры данных.

    Args:
        transaction: Словарь с данными о транзакции

    Returns:
        Сумма в рублях (float) или None при ошибках
    """
    # Проверяем наличие operationAmount
    if not transaction.get('operationAmount'):
        return None

    operation_amount = transaction['operationAmount']

    # Безопасное извлечение amount
    try:
        amount_str = operation_amount.get('amount')
        if not amount_str:
            return None
        amount = float(amount_str)
    except (TypeError, ValueError):
        return None

    # Безопасное извлечение currency
    currency_info = operation_amount.get('currency')
    if not currency_info:
        return None

    currency = currency_info.get('code', 'RUB').upper()

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