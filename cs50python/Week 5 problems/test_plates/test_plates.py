from plates import is_valid

def test_two_letters():
    assert is_valid("aa1234") == True
    assert is_valid("a1234") == False
    
def test_6_char():
    assert is_valid("aa123") == True
    assert is_valid("a") == False
    assert is_valid("aa123452") == False

def test_numbers():
    assert is_valid("aa1223")  == True
    assert is_valid("aa12a1") == False
    assert is_valid("aa02a1") == False
    
def test_punt():
    assert is_valid("aa1234") == True
    assert is_valid("aa,123") == False