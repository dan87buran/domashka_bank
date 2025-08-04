import pandas as pd
from typing import List, Dict, Any


def read_csv_transactions(file_path: str) -> List[Dict[str, Any]]:
    """
    Считывает финансовые операции из CSV-файла.

    Args:
        file_path: Путь к CSV-файлу с транзакциями

    Returns:
        Список словарей с транзакциями
    """
    return pd.read_csv(file_path).to_dict('records')


def read_excel_transactions(file_path: str) -> List[Dict[str, Any]]:
    """
    Считывает финансовые операции из Excel-файла.

    Args:
        file_path: Путь к Excel-файлу с транзакциями

    Returns:
        Список словарей с транзакциями
    """
    return pd.read_excel(file_path).to_dict('records')