import sys
try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("too few arguments")
#Notice that sys.argv[1] is where David is being stored. 
#Why is that? Well, in prior lessons, you might remember that lists start at the 0th element.
#What do you think is held currently in sys.argv[0]? If you guessed name.py, you would be correct!

if len(sys.argv) < 2:
    sys.exit("too few arguments")
for arg in sys.argv[1:]:
    print("hello, my name is", arg)
