from plates import is_valid

def test_start():
    assert is_valid("AB1234") == True
    assert is_valid("A12345") == False
    assert is_valid("123456") == False

def test_lenth():
    assert is_valid("CS05") == False
    assert is_valid("AB") == True
    assert is_valid("AB12") == True
    assert is_valid("AB123456") == False

def test_end():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False
    assert is_valid("A222A") == False

def test_not_alpha():
    assert is_valid("ABC12?") == False
    assert is_valid(" AB123") == False
    assert is_valid(",AB.23") == False
    assert is_valid(".AB23") == False