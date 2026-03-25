import datetime as dt
from inflect import engine
import sys
import re

#常规方法写一遍，OOP写一遍
def main():
    #input birthday和get nowday
    birthDate = input("Date of birth: ").strip()
    nowDate = dt.date.today()

    #1 确认输入无异常，并基于date的方法，得到timedelta object
    validDate = r"^(19\d\d|20\d\d)-(0[1-9]|1[0-2])-([0-2][0-9]|3[0-1])$"
    minutes = calculate_minute(validDate, birthDate)*24*60
    #3 数字转英文挑格式并print
    print(engine().number_to_words(minutes).replace(" and", "").capitalize(), "minutes")

def calculate_minute(validDate, birthDate):
    if birthDate := re.search(validDate, birthDate):
        #2 将search得到的string转化为date类型，然后和today相减，追加timedelta object 的特有attributes:days
        return (dt.date.today() - dt.date(int(birthDate.group(1)), int(birthDate.group(2)), int(birthDate.group(3)))).days
    else:
        sys.exit("Invaild input")
    

if __name__ == "__main__":
    main()
