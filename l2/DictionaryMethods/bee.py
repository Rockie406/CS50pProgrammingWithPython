WORDS = {
    "PAIR": 4, "HAIR": 4, "CHAIR": 5
}

def main():
    print("Welcome to the Spelling Bee")
    print("Your letters are: A I P C R H G")

    '''while len(WORDS) > 0:
        print(f"{len(WORDS)} words left!")
        guess = input("Guess a word: ")

        if guess == "GRAPHIC":
            WORDS.clear()
            print("You've won")

        if guess in WORDS.keys():
            guesses = WORDS.pop(guess)
            print(f"Good job, you scored {guesses} points")
'''
    for words, scores in WORDS.items():
        print(f"{words} was worth {scores} points")
    print("That's the game!")    

main()