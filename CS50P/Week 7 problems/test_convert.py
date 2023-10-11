from convert import convert
import pytest

def correct():
    assert convert("9 AM to 5 PM") == "9:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "9:00 to 17:00"
    assert convert("9:15 AM to 5 PM") == "9:15 to 17:00"
    assert convert("9 AM to 5:15 PM") == "9:00 to 17:15"
    
def wrong():
    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ValueError):
        convert("9am to 7pm")
    with pytest.raises(ValueError):
        convert("9 AM to 17 PM")
    with pytest.raises(ValueError):
        convert("")
