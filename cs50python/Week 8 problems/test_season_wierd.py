from seasons import turn_to_words
from datetime import date
import pytest


def test_():
    assert turn_to_words(date.fromisoformat("1998-09-01")) == "Thirteen million, two hundred thirteen thousand, four hundred forty minutes"
    assert turn_to_words(date.fromisoformat("2021-10-16")) == "One million, fifty-one thousand, two hundred minutes"

def test_exit():
    with pytest.raises(ValueError):
        turn_to_words(date.fromisoformat("cat"))