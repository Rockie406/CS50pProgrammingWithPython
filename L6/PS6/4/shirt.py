import sys
from PIL import Image, ImageOps

def main():
    cla_check(4, 2)
    with Image.open("shirt.png") as shirt:
        shirtSize = shirt.size
        with Image.open(sys.argv[1]) as img:
            body = ImageOps.fit(img, shirtSize)
            body.paste(shirt, shirt)
            body.save(sys.argv[2])

def cla_check(suffix_count, argument_count):
    if len(sys.argv) != (argument_count + 1):
        sys.exit(f"{argument_count} argument only")
    elif sys.argv[1][-suffix_count:] != sys.argv[2][-suffix_count:]:
        sys.exit("input's name doesn't have the same extension as the output's name")

    for index in range(argument_count):
        if sys.argv[index+1][-4:].lower() != ".jpg" and sys.argv[index+1][-4:].lower() != ".png" and sys.argv[index][-5:].lower() != ".jpeg":
            sys.exit(".jpg .png .jpeg only")
        

    try:
        with open(sys.argv[1]) as file:
            pass
    except FileNotFoundError:
        sys.exit("file does not exit")
    except IndexError:
        sys.exit("")
#检验首先针对argv对应的list，无误则进一步检查list的内容

if __name__ == "__main__":
    main()