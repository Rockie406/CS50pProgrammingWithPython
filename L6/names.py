
lines = []

with open("names.txt", "r") as file:

    for name in file:
        lines.append(name.strip())

    for line in sorted(lines):
        print(f"hello, {line}")
