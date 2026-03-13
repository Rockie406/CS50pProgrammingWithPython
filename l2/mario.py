'''def main():
    print_column(3)
    print_row(4)

def print_column(height):
    for _ in range(height):
        print("#")

def print_row(width):
    print("?" * width)

main()'''

def main():
    print_square(3)

def print_square(size):
    for _ in range(size):
        for _ in range(size):
            print("#", end="") #这个inner循环也可以通过print（”#“ * width）实现
        print()

main()
