from jar import Jar
import pytest

def test_init():
    with pytest.raises(ValueError):
        Jar("cat")
        Jar("-1")

def test_str():
    jar = Jar("3")
    jar.deposit(3)
    assert jar.__str__() == "🍪🍪🍪"

def test_deposit():
    jar = Jar("3")
    jar.deposit(3)
    assert jar.size == 3

    with pytest.raises(ValueError):
        jar.deposit(4)