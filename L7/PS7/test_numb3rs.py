from numb3rs import validate
import pytest

def test_format():
    assert validate("123456789") == False
    assert validate("123,23,12,13") == False
    assert validate("123..23.13.12") == False

def test_value():
    assert validate("123.456.789.012") == False
    assert validate("8.8.8.112") == True
    assert validate("255.255.256.255") == False
