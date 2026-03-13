import random

def main():
    while True:
        level = positive_number_input("Level: ")

        if level > 0:
            rand = random.randint(1, level)
            guess = positive_number_input("Guess: ")
            #guess也要实现这个
            while True:
                if guess > 0:
                    if guess < rand:
                        print("Too small!")
                        guess = positive_number_input("Guess: ")
                    elif guess > rand:
                        print("Too large!")
                        guess = positive_number_input("Guess: ")
                    else:
                        print("Just right!")
                        break
                elif guess <= 0:
                    guess = positive_number_input("Guess: ")
            break
        
def positive_number_input(name):
    try:
        return int(input(name).strip())
    except ValueError:
        return 0

main()                    