def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if start_with(s) and length(s) and end_number(s) and no_spaces(s):
        return True
    else:
        return False
    
def start_with(s):
#“All vanity plates must start with at least two letters.”
    index = 0
    for character in s:
        if index < 2:
            if character.isalpha():
                index += 1
            else:
                return False
        if index == 2:
            return True
            
#“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
def length(s):
    if 2<=len(s)<=6:
        return True
    else:
        return False
#“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
def end_number(s):
    index = 0
    for character in s:
        if index < 2:
            index += 1
        elif index >= 2:
            if  character.isdecimal() and not s[index - 1].isdecimal() and character == "0":
                return False

            elif not character.isdecimal() and s[index - 1].isdecimal():
                return False
            else:
                index += 1
    return True

#“No periods, spaces, or punctuation marks are allowed.”"""
def no_spaces(s):
    if s.isalnum():
        return True
    else:
        return False

if __name__ == "__main__":
    main()
