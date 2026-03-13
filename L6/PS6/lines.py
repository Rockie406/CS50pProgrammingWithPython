import sys
i = 0

try:
    file = open(sys.argv[1], "r")
except IndexError:
    sys.exit("1 argument needed")
except FileNotFoundError:
    sys.exit("file doesn't exit")

if len(sys.argv) > 2:
    sys.exit("too many arguments(>1)") 
elif sys.argv[1][-3:] != ".py":
    sys.exit(".py only")

for row in file:
    if row.isspace():
        i += 0
    elif row.lstrip()[0] == "#":
        i += 0
    else:
        i += 1
print(i)
