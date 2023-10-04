from fuel import convert
import pytest

def test_input():
    assert convert("2/2") == 1
    assert convert("100/2") == 50
    
def test_input_alpha():
    with pytest.raises(ValueError) as execinfo:
        convert("a/2")
    assert str(execinfo.value) == "Inputs must be integer" 
    with pytest.raises(ValueError) as execinfo:
        convert("a/2")
    assert str(execinfo.value) == "Inputs must be integer" 