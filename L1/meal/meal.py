def main():
    time = input("What time is it? ")
    if convert(time) >= 7 and convert(time) <= 8:
        print("breakfast time")
    elif convert(time) >= 12 and convert(time) <= 13:
        print("lunch time")
    elif convert(time) >= 18 and convert(time) <= 19:
        print("dinner time")


def convert(time):
    h, m = time.split(":")
    return  float(h) + float(m)/60

if __name__ == "__main__":
    main()