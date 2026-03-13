
#wherein each of X and Y is a positive integer
#and then outputs, as a percentage rounded to t>
def main():
    while True:
    #输入分数
        try:
            fraction = input("Fractions: ")
            value = convert(fraction)
        except ZeroDivisionError:
            print("ZeroDivisionError")
            value = -1
        except ValueError:
            print("ValueError")
            value = -1#本质是非int和负>

        if 0 <= value <= 100:
            print(gauge(value))
            break


    #区分分子除号分母

def convert(fraction):
        x, y = fraction.split("/")
        value = round(int(x) / int(y) * 100)

        if value > 100:
            raise ValueError
        elif value < 0:
            raise ValueError
        else:
            return value
    


def gauge(value):
    if 0 <= value <= 1:
        return "E"
    elif 99 <= value <= 100:
        return "F"
    else:
        return f"{value}%"
##try里面的内容尽可能少

if __name__ == "__main__":
    main()
    #输出
#check50 cs50/problems/2022/python/fuel