
#wherein each of X and Y is a positive integer
#and then outputs, as a percentage rounded to t>
def main():
    while True:
    #输入分数
        fraction = input("Fractions: ")
    #区分分子除号分母
        try:
            x, y = fraction.split("/")
            value = round(int(x) / int(y), 2)
            if value > 1:
                pass
            elif value < 0:
                raise ValueError
            else:
                break
        except ZeroDivisionError:
            print("ZeroDivisionError")
        except ValueError:
            print("ValueError")#本质是非int和负>
       


    if 0 <= value <= 0.01:
        print("E")
    elif 0.99 <= value <= 1:
        print("F")
    else:
        print(f"{int(value * 100)}%")
##try里面的内容尽可能少
main()
    #输出
#check50 cs50/problems/2022/python/fuel