import pytest
import os
from src.file_reader import read_json_file, read_csv_file


def test_read_json_file(tmp_path):
    # Создаем временный JSON файл
    test_data = [{'test': 'data'}]
    file_path = tmp_path / "test.json"

    import json
    with open(file_path, 'w') as f:
        json.dump(test_data, f)

    result = read_json_file(str(file_path))
    assert result == test_data


def test_read_csv_file(tmp_path):
    # Создаем временный CSV файл
    file_path = tmp_path / "test.csv"

    with open(file_path, 'w', newline='') as f:
        import csv
        writer = csv.DictWriter(f, fieldnames=['test'])
        writer.writeheader()
        writer.writerow({'test': 'data'})

    result = read_csv_file(str(file_path))
    assert len(result) == 1
    assert result[0]['test'] == 'data'