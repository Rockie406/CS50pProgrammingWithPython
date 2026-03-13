def main():
    pace = get_pace(miles = 26.2, minutes = 00)
    print(f"You need to run each mile in {round(pace, 2)} minutes.")

def get_pace(miles, minutes):
    if not minutes > 0:
        raise ValueError("Invalid value for minutes")
    #raise 和 handle有什么区别:
    #handle针对程序error，raise针对valid但是不符合作者期望/实际的情况
    
    return minutes / miles

main()