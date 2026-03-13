def main():
    names = ["Mario", "Luigi", "Daisy", "Yoshi", "Bowser"]
    for name in names:
        print(write_letter(name, "Princess Peach"))
    
def write_letter(receiver, sender):
    return f"""
+~~~~~~~~~~~~~~~~~~~~~~~+
Dear {receiver}:

You are cordially invited to a ball at
Peach's Castle this evening, 8:00 PM.

Sincerely,
{sender}
"""

main()