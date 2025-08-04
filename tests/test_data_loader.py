import unittest
from unittest.mock import patch, MagicMock
from src.data_loader import read_csv_transactions, read_excel_transactions


class TestDataLoader(unittest.TestCase):
    @patch('pandas.read_csv')
    def test_read_csv_transactions(self, mock_read_csv):
        """Тест чтения CSV-файла"""
        mock_data = MagicMock()
        mock_data.to_dict.return_value = [{'test': 'data'}]
        mock_read_csv.return_value = mock_data

        result = read_csv_transactions('test.csv')

        mock_read_csv.assert_called_once_with('test.csv')
        self.assertEqual(result, [{'test': 'data'}])

    @patch('pandas.read_excel')
    def test_read_excel_transactions(self, mock_read_excel):
        """Тест чтения Excel-файла"""
        mock_data = MagicMock()
        mock_data.to_dict.return_value = [{'test': 'data'}]
        mock_read_excel.return_value = mock_data

        result = read_excel_transactions('test.xlsx')

        mock_read_excel.assert_called_once_with('test.xlsx')
        self.assertEqual(result, [{'test': 'data'}])