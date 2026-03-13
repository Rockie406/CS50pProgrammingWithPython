
import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(html):
    embedUrl = re.search(r"^iframe src=(\"https?://www.youtube.com/embed/w\")$", html)
    #针对SRC前后可能存在的字段，还需要完善regexe