'''i = 0
while i < 3:
    print("meow")
    i += 1 '''

'''for _ in range(3):
    print("meow\n" * 3, end = "")'''

def main():
    meow(get_number())

def meow(n):
    for _ in range(n):
        print("meow")

def get_number():
    while True:
        x = int(input("what is the number? "))
        if x > 0:
            break
    return x

main()


