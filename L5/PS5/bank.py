def main():
    greeting = input("Greeting: ")
    money = value(greeting)
    print(f"${money}")
    

def value(greeting):
    greeting = greeting.lower()
    greeting_hello = greeting.removeprefix("hello")
    greeting_h = greeting.lstrip("h")
    if greeting != greeting_hello:#get the first word
        return 0
    elif greeting != greeting_h:#get the first word
        return 20
    else:
        return 100 #如果lstrip前后有别，则可认为hello/h存在

if __name__ == "__main__":
    main()

#check50 cs50/problems/2022/python/bank
#submit50 cs50/problems/2022/python/bank
