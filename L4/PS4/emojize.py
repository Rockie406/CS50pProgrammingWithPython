import emoji


def main():
    code = input("Input: ").strip()
    if code.count("_") > 0:
        lang = "alias"
    else:
        lang = "en"
        if emoji.emojize(code, language = lang) == code:
            lang = "alias"

    print(emoji.emojize(f"Output: {code}", language = lang))
main()