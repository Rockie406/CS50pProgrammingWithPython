from working import convert
import pytest

def test_value():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"

def test_AMPM():
    with pytest.raises(ValueError):
        convert("9:00 to 5:00 PM")
        convert("9:00 PM to 5:00")
        convert("9:00 to 5:00")

def test_time():
    with pytest.raises(ValueError):
        convert("13:00 AM to 5:00 PM")
        convert("9:00 PM to 13:00 PM")
        convert("12:60 AM to 5:00 PM")
def test_to():
    with pytest.raises(ValueError):
        convert("9:00 AM 5:00 PM") == "09:00 to 17:00"
        convert("9 AM 5 PM") == "09:00 to 17:00"
        convert("9:00 AM 5 PM") == "09:00 to 17:00"
        convert("9 AM 5:00 PM") == "09:00 to 17:00"