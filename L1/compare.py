'''x = int(input("what is x? "))
y = int(input("what is y? "))
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")'''

# This program can be improved by not asking three consecutive questions. 
# After all, not all three questions can have an outcome of true! 

'''x = int(input("what is x? "))
y = int(input("what is y? "))
if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")'''

score = int(input("Score: "))
'''if score <= 100 and score >= 90:
    print("A")
elif score < 90 and score >= 80:
    print("B")
elif score < 80 and score >= 70:
    print("C")
elif score < 70 and score >= 60:
    print*("D")
else:
    print("F")'''
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")