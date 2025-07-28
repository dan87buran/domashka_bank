import pytest
from datetime import datetime
from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def sample_transactions():
    return [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2023-01-01T00:00:00.000000",
            "amount": 100
        },
        {
            "id": 2,
            "state": "PENDING",
            "date": "2023-01-02T00:00:00.000000",
            "amount": 200
        },
        {
            "id": 3,
            "state": "EXECUTED",
            "date": "2023-01-03T00:00:00.000000",
            "amount": 300
        },
        {
            "id": 4,
            "date": "2023-01-04T00:00:00.000000",
            "amount": 400
        }
    ]


class TestFilterByState:
    @pytest.mark.parametrize("state,expected_count", [
        ("EXECUTED", 2),  # Изменили ожидание с 1 на 2
        ("PENDING", 1),
        ("CANCELLED", 0),
        ("", 0)
    ])
    def test_filter_counts(self, sample_transactions, state, expected_count):
        result = filter_by_state(sample_transactions, state)
        assert len(result) == expected_count

    def test_filter_content(self, sample_transactions):
        result = filter_by_state(sample_transactions, "EXECUTED")
        assert all(t["state"] == "EXECUTED" for t in result)
        assert {t["id"] for t in result} == {1, 3}

    def test_empty_input(self):
        assert filter_by_state([], "EXECUTED") == []


class TestSortByDate:
    def test_sort_ascending(self, sample_transactions):
        result = sort_by_date(sample_transactions, descending=False)
        dates = [datetime.fromisoformat(t["date"]) for t in result]
        assert dates == sorted(dates)

    def test_sort_descending(self, sample_transactions):
        result = sort_by_date(sample_transactions, descending=True)
        dates = [datetime.fromisoformat(t["date"]) for t in result]
        assert dates == sorted(dates, reverse=True)

    def test_same_dates(self, sample_transactions):
        test_data = [dict(t) for t in sample_transactions]
        # Устанавливаем одинаковые даты для всех транзакций
        same_date = "2023-01-01T00:00:00.000000"
        for t in test_data:
            t["date"] = same_date

        result = sort_by_date(test_data)

        # Проверяем, что все даты одинаковы
        dates = {t["date"] for t in result}
        assert len(dates) == 1
        assert same_date in dates

    def test_invalid_date_format(self, sample_transactions):
        test_data = [dict(t) for t in sample_transactions]
        test_data[0]["date"] = "invalid-date"
        with pytest.raises(ValueError):
            sort_by_date(test_data)

    def test_missing_date_field(self, sample_transactions):
        test_data = [dict(t) for t in sample_transactions]
        del test_data[0]["date"]
        with pytest.raises(ValueError):
            sort_by_date(test_data)

    def test_empty_input(self):
        assert sort_by_date([]) == []