from fuel import convert

def test_input():
    assert convert("2/2") == 2, 2
    assert convert("1/a") == 1, "a"