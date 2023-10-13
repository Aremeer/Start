from response import check

def test_():
    assert check("malan@harvard.edu") == "Valid"
    assert check("artem.davydov3@gmail.com") == "Valid"
    assert check("malan@@@harvard.edu") == "Invalid"
    assert check("arte m.davy dov3@@.gm ail..com") == "Invalid"