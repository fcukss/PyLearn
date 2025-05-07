import pytest
from datetime import date
from seasons import get_minutes, is_valid

def test_is_valid_valid_date():
    assert is_valid("2000-01-01") == date(2000, 1, 1)

def test_is_valid_invalid_date(monkeypatch):
    with pytest.raises(SystemExit):
        is_valid("January 1, 2000")

def test_get_minutes(monkeypatch):
    test_input = "2023-01-01"
    monkeypatch.setattr("builtins.input", lambda _: test_input)
    today = date.today()
    dob = date.fromisoformat(test_input)
    expected_minutes = abs((today - dob).days) * 24 * 60
    assert get_minutes() == expected_minutes