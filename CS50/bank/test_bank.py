from bank import value

def test_hello():
    assert value("hello") == 0

def test_hey():
    assert value('hey') == 20

def test_other_name():
    assert value("bill")==100