import sys
from pyfiglet import Figlet
import random

def main():
    if len(sys.argv) == 1:
        fig_output(random.choice(Figlet().getFonts()))
    elif len(sys.argv) == 3:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            if sys.argv[2] in Figlet().getFonts():
                fig_output(sys.argv[2])
            #figlet.setFont(font = sys.argv[2])
            else:
                sys.exit("not the name of a font")
        else:
            sys.exit("-f or --font only")
    else:
        sys.exit("Invalid 1 arguement")

def fig_output(font):
    ordinary = input("Input: ")
    figlet = Figlet()
    figlet.setFont(font = font)
    print(figlet.renderText(ordinary))
main()