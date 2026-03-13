
from random import randint

def main():
    
    score = 0
    questionTime = 0
    level = get_level()
    while questionTime < 10:
        x = generate_integer(level)
        y = generate_integer(level)
        score += calculate(x, y)
        questionTime += 1
    print(score)


#这种模块化的思路有意思，即将输入合法性判断集中在某个函数，而不是在分散的if中体现
def get_level():
    while True:
        try:
            level = int(input("Level: ").strip())
        except ValueError:
            level = None
        if level == 1 or level == 2 or level == 3:
            return level
        
def generate_integer(level):
    if level == 1:
        return round(randint(0, 9))
    elif level == 2:
        return round(randint(10, 99))
    else:
        return round(randint(100, 999))
def calculate(x, y):
    wrongTime = 0
    while wrongTime < 3:
        try:
            calculate = float(input((f"{x} + {y} = ")))
        except ValueError:
            calculate = None 
        if calculate == (x + y):
            return 1
        elif calculate != (x + y):
            print("EEE")
            wrongTime += 1
    print((f"{x} + {y} = {x + y}"))
    return 0

if __name__ == "__main__":
    main()