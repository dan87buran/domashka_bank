import pytest
from unittest.mock import mock_open, patch
from src.utils import load_transactions

@pytest.mark.parametrize("content,expected", [
    ('[{"id": 1}]', [{"id": 1}]),
    ('{}', []),
    ('', []),
    ('invalid json', []),
])
def test_load_transactions(content, expected):
    with patch('builtins.open', mock_open(read_data=content)):
        assert load_transactions('any_path.json') == expected