import csv
students = []
name = input("what is your name? ")
home = input("where is your home? ")
with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames = ["name", "home"])
    writer.writerow({"name": name, "home": home})

#        studentss[name] = home
#for student in sorted(studentss):
#    print(f"{student} is in {studentss[student]}")
#codes above are easier than in notes, but the function  sorted()  is not avaliable for a dict.
