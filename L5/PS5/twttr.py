def main():
    with_vowel = input("Input: ")
    without_vowel = shorten(with_vowel)
    print(f"Output: {without_vowel}")


def shorten(word):
    vowels = "AEIOUaeiou"
    result = ""
    for c in word:
        if c not in vowels:
            result += c
    return result

if __name__ == "__main__":
    main()
