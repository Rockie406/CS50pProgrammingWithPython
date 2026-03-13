import re

name = input("What's your name? ").strip()
#(...)means a group
matches = re.search(r"^(.+), *(.+)$", name)

if matches := re.search(r"^(.+), *(.+)$", name):
    last, first = matches.groups()
    #name = f"{first} {last}"
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")