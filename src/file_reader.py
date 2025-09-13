import json
import csv
from typing import List, Dict
import openpyxl


def read_json_file(file_path: str) -> List[Dict]:
    """
    Читает данные из JSON файла

    Args:
        file_path: Путь к JSON файлу

    Returns:
        Список словарей с данными о транзакциях
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def read_csv_file(file_path: str) -> List[Dict]:
    """
    Читает данные из CSV файла

    Args:
        file_path: Путь к CSV файлу

    Returns:
        Список словарей с данными о транзакциях
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except (FileNotFoundError, csv.Error):
        return []


def read_xlsx_file(file_path: str) -> List[Dict]:
    """
    Читает данные из XLSX файла

    Args:
        file_path: Путь к XLSX файлу

    Returns:
        Список словарей с данными о транзакциях
    """
    try:
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active

        headers = [cell.value for cell in sheet[1]]
        data = []

        for row in sheet.iter_rows(min_row=2, values_only=True):
            data.append(dict(zip(headers, row)))

        return data
    except (FileNotFoundError, openpyxl.utils.exceptions.InvalidFileException):
        return []