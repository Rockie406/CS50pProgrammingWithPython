from calculator import square
import pytest


def test_positive():
    assert square(2) == 4
    assert square(3) == 9
def test_negative():        
    assert square(-2) == 4
    assert square(-3) == 9
def test_zero():
    assert square(0) == 0
def test_str():
    #这里是预期输入str，引用的calculator会报valueerror，
    with pytest.raises(TypeError):
        square("cat")

#main函数和引用都不需要

#if __name__ == "__main__":
   # main()