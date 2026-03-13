'''#hello world
x = int(input("what is x? "))
y = int(input("what is y? "))
z = x + y
print(z)
#situation等可与with/about连用，reasons等可与for等连用？reason本身隐含了for的目的性？
#get the user's input
x = float(input("what is x?"))
y = float(input("what is y"))
#create a rounded result
z = round(x + y)
#print  the result
print(f"{z:,}")'''

'''#Get the users input
x = float(input("what is x? "))
y = float(input("what is y? "))
#calculate the result
z = x / y
#print the result
print(f"{z:.2f}")'''

#calculate the square of x
def main():
    x = int(input("what is x? "))
    print("x square is,", square(x))
def square(x):
    return x*x
main()