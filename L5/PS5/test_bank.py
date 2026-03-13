from bank import value
import pytest

#Only main should call print.
#case-insensitively

def test_type():
    assert value("123") == 100

def test_none():
    assert value("") == 100

def test_hello():
    assert value("hello, xyz") == 0

def test_h():
    assert value("hi, xyz") == 20
    assert value("hanimah") == 20

def test_case():
    assert value("Hello, xyz") == 0
    assert value("Hi, xyz") == 20