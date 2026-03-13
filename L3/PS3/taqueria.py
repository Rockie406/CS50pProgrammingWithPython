 #After each inputted item, display the total cost of all items inputted thus far, done
 #prefixed with a dollar sign ($) and formatted to two decimal places. done
 # Treat the user’s input case insensitively. Ignore any input that isn’t an item. done
 # Assume that every item on the menu will be titlecased.done
def main():
    menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
    total = 0
    while True:
        try:
            meal = input("Item: ")
        except EOFError:
            break
        try:
            a, b = meal.split(" ")
        except ValueError:
            meal = meal.lower().capitalize()
        else:

            meal = a.lower().capitalize() + " " + b.lower().capitalize()
        # print(meal)
        for item in menu:
            if meal == item:
                a = menu[meal]
                b = total
                total += menu[meal]
                print(f"Total: ${total:.2f}")
main() 