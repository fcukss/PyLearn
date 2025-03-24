from plates import is_valid

import pytest


def test_valid_results():
    assert is_valid("CS50") == True

def test_invalid_res():
    assert is_valid("CS05") == False

def test_number():
    with pytest.raises(AttributeError):
        is_valid(2823)

def test_long_number():
    assert is_valid("24u235932523532523523") == False
