import pytest
from seasons import calculate_minute

'''def test_invalidInput():
    with pytest.exit("Invalid input"):
        calculate_minute("1991-13-01")
        calculate_minute("1991-11-32")
        calculate_minute("2025-11-11")'''
ValidDate = r"^(19\d\d|20[0-2][0-6])-(0[1-9]|1[0-2])-([0-2][0-9]|3[0-1])$"
def test_validInput():
    assert calculate_minute(ValidDate, "2025-03-21") == 365
    assert calculate_minute(ValidDate, "2024-03-21") == 730

