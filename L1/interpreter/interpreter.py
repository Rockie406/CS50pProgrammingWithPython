def main():
    formula = input("Formula: ")
    x, y, z = formula.split(" ")
    if y == "+":
        print(float(x) + float(z))
    elif y == "-":
        print(float(x) - float(z))
    elif y == "*":
        print(float(x) * float(z))
    elif y == "/" and z != 0:
        print(float(x) / float(z))



main()
    #check50 cs50/problems/2022/python/interpreter
    #submit50 cs50/problems/2022/python/interpreter