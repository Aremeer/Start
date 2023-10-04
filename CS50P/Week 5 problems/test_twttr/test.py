from twttr import shorten

def test_lower():
    assert shorten("artem") == "rtm"
    assert shorten("hello world") == "hll wrld"
    
def test_upper():
    assert shorten("DAVID") == "DVD"
    assert shorten("HELLO WORLD") == "HLL WRLD"