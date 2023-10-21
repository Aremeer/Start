from numb3rs import validate

def test_main():
    assert validate("243.54.1.1") == True
    assert validate("267.1.1.1") == False
    assert validate("1.344.1.1") == False
    assert validate("1.1.444.1") == False
    assert validate("1.1.1.444") == False
    assert validate("cat") == False
    assert validate("my name is happy") == False
    assert validate("1.1.1.1.1.1") == False
