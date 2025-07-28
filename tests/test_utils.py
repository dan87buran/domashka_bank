import unittest
from unittest.mock import mock_open, patch
from src.utils import load_transactions


class TestUtils(unittest.TestCase):
    @patch('builtins.open', mock_open(read_data='[{"id": 1}]'))
    def test_load_transactions_valid(self):
        result = load_transactions('dummy.json')
        self.assertEqual(result, [{"id": 1}])

    @patch('builtins.open', mock_open(read_data='{}'))
    def test_load_transactions_not_list(self):
        result = load_transactions('dummy.json')
        self.assertEqual(result, [])

    def test_load_transactions_file_not_found(self):
        result = load_transactions('nonexistent.json')
        self.assertEqual(result, [])
