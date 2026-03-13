from twttr import shorten
import pytest

def test_none():
    assert shorten("") == ""

def test_type():
    assert shorten("123") == "123"

def test_word():
    assert shorten("Twitter") == "Twttr"
    assert shorten("CS50") == "CS50"
    assert shorten("TwItter") == "Twttr"

def test_sentence():
    assert shorten("What's your name?") == "Wht's yr nm?"