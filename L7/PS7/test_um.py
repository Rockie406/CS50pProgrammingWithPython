import pytest
from um import count

def test_value():
    assert count("um.") == 1
    assert count("thanks for, um, helping") == 1
    assert count("ah, um...")
    assert count("um") == 1
    assert count("um, it's nice to see you, ylh, but I have sth more, um, attractive to be done. hope you have a nice day, um...") == 3

def test_none():
    assert count("yummy") == 0
    assert count("cum, yummy") == 0

def test_case():
    assert count("Um.") == 1
    assert count("thanks for, uM, helping") == 1
    assert count("ah, UM...")
    assert count("UM") == 1

