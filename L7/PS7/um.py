import re

def main():
    print(count(input("Text: ")))

def count(text):
    text = text.lower()
    if umAll := re.findall(r"(^um$)|(^um[^\w])|([^\w]um[^\w])", text):
        return len(umAll)
    else:
        return 0
    

if __name__ == "__main__":
    main()