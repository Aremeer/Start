from seasons import code
from datetime import date
import pytest


def test_():
    assert code("1998-09-01") == "Thirteen million, two hundred thirteen thousand, four hundred forty minutes"
    assert code("2021-10-16") == "One million, fifty-one thousand, two hundred minutes"

def test_exit():
    with pytest.raises(ValueError):
        code(date.fromisoformat("cat"))