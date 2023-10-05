from fuel import convert
from fuel import gauge
import pytest

def test_input():
    assert convert("2/2") == 100
    assert convert("50/100") == 50

def test_input_alpha():
    with pytest.raises(ValueError):
        convert("a/2")
    with pytest.raises(ValueError):
        convert("a/2")

def test_input_x_greater_than_y():
    with pytest.raises(ValueError):
        convert("2/1")
    with pytest.raises(ValueError):
        convert("100/50")
        
def test_zero_div():
    with pytest.raises(ZeroDivisionError):
        convert("2/0")
        

def 