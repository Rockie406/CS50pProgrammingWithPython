'''name = input("what is your name? ")
if name == "harry":
    print("Gryffindor")
elif name == "hermione":
    print("Gryffindor")
elif name == "ron":
    print("Gryffindor")
elif name == "draco":
    print("slythertin")
else:
    print("who? ")
if name == "harry" or name == "hermione" or name == "ron":
    print("Gryffindor")
elif name == "draco":
    print("slythertin")
else:
    print("who? ")'''

name = input("what's your name? ")

match name:
    case "Henrry" | "Hermione" | "Ron":
        print("Gryffindor")
    
    case _:
        print("who?")