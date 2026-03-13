def main():
    x = int(input("what is x? "))
    
    if is_even(x):
        print("x is even")
    else:
        print("x is odd")

def is_even(x):
    '''if x % 2 == 0:
        return True
    else:
        return False'''
    return True if x % 2 == 0 else False

main()
