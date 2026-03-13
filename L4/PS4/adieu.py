import inflect
def main():
    p = inflect.engine()
    song = ""
    names = []
    while True:
        try:
            name = input("Name: ").strip()
        except EOFError:
            song = p.join(names)
            print("Adieu, adieu, to " + song)
            break
        names.append(name)
        
    #难点在于and随时保持n-1位
if __name__ == "__main__":
    main()