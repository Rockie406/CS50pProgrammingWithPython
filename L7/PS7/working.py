import re

def main():
    print(convert(input("Hours: ")))

def convert(twelveHour):
    #能否存在二级括号, 能
    #二级括号下包含的一级括号该如何被interpreter读取？
    #记得提高对input格式的兼容性
    if twentyfourHour := re.search(r"^((?:[0-9]|1[0-2])(?::[0-5][0-9])? (?:AM|PM)) to ((?:[0-9]|1[0-2])(?::[0-5][0-9])? (?:AM|PM))$", twelveHour):

        return (split(twentyfourHour, 1) + " to " + split(twentyfourHour, 2))
    else:
        raise ValueError

def split(searchObject, groupNumber):
    time, meridiem = searchObject.group(groupNumber).split(" ")
    try:
        hour, minute = time.split(":")
    except ValueError:
        hour = time
        minute = "00"
    #这个地方还是乱乱的
    if meridiem == "PM":
        hour = int(hour) + 12
    if int(hour) in (12, 24) and minute == "00":
        hour = int(hour) - 12

    return f"{int(hour):02}:{minute}"


if __name__ == "__main__":
    main()