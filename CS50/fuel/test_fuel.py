import fuel

import pytest

def test_convert():
    assert fuel.convert("3/4")==75

def test_error():
    with pytest.raises(ValueError):
        fuel.convert("5/4")


def test_gauge():
    assert fuel.gauge(50)=="50%"
