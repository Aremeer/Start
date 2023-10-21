from bank import value

def test_lower():
    assert value("Hello, Newman") == (0)
    assert value("howdy") == (20)
    assert value("yo") == (100)

def test_upper():
    assert value("HELLO") == (0)
    assert value("HOWDY") == (20)
    assert value("YO") == (100)

def test_else():
    assert value("1234") == (100)
    assert value(",./") == (100)

def test_phrase():
    assert value("yo buddy") == (100)
