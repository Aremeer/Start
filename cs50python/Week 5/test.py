from professor import get_level 
def test_get_level():
    assert get_level(1) == 1
    assert get_level(2) == 2
    assert get_level(3) == 3
    assert get_level("a") != "a"
    assert get_level(0) != 0