import random

cards = ["jack", "queen", "king"]

def main():
    random.seed(1)#to be sure of the output
    print(random.choices(cards, weights = [75, 20, 5], k = 2))
    print(random.sample(cards, k = 2))


main()