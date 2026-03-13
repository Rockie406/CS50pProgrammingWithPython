

from hello import hello
  
  
def test_default():
    assert hello() == "hello, world"
  
  
def test_argument():
    assert hello("David") == "hello, David"

#Now, typing pytest test in the terminal, 
# you can run the entire test folder of code.