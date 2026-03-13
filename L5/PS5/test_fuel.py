from fuel import convert
from fuel import gauge
import pytest

def test_division():

    with pytest.raises(ValueError):
        convert("1/1.5")
        convert("1.100")
        convert("cat")


def test_xy():

    with pytest.raises(ValueError):
        convert("-1/100")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

    assert convert("0/4") == 0
    assert convert("1/4") == 25
    assert convert("2/4") == 50
    assert convert("3/4") == 75
    assert convert("4/4") == 100

    assert gauge(1) == "E"
    assert gauge(25) == "25%"
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"
    assert gauge(99) == "F"



