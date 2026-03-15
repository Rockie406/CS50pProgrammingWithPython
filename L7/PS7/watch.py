import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(html):
    # 针对SRC前后可能存在的字段，还需要完善regexe
    if embedUrl := re.search(
        #之前一直报错，是因为^$锚定死了首尾字符，导致一直对不上
        r"iframe.+src=\"(https?://(?:www\.)?youtu)be\.com/embed(/\w+)\"", html
    ):
        return "https://youtu.be" + embedUrl.group(2)


if __name__ == "__main__":
    main()

