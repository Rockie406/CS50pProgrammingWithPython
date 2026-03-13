##理不全逻辑关系，修改时多次盲人摸象，有点痛苦
def main():                                  
    months = [
        "January",                               
        "February",                               
        "March",
        "April",                                  
        "May",                                    
        "June",
        "July",                                   
        "August",                                 
        "September",
        "October",                                
        "November",                             
        "December"
    ]
   
    while True:  
        error_time = 0  
        #1. 输入
        date = input("Date: ").strip()#可以搞个“纯净input”的函数了
        #1.1 区分输入方式和元素（包括illegal的）
        #illegal如后：date>31, month>12, /格式用字母月， 空格格式日月对调，空格格式无逗号
        if not date.find("/") == -1 or not date.find(",") ==-1:
            try:
                month, day, year = date.split("/")
            #if September 8, 1636  inputed
            except ValueError:
                monthday, year = date.split(", ")
                month, day = monthday.split(" ")

            
            try:
                int(day)
                #排除day是月份的情况
            except ValueError:
                pass
            else:
                if int(day) > 31:
                    error_time += 1
                else:
                    day = pad(day) #return为什么没有break外层循环,因为return不是所有情况都发生

                if (month.isalpha() and not date.find(", ") == -1):
                    month = pad(word_to_number(month, months))
                elif (month.isnumeric() and not date.find("/") == -1):
                    month = pad(month)
                    if int(month) > 12:
                        error_time += 1
                elif month.isalpha():
                    error_time += 1

                if error_time == 0:
                    print(f"{year}-{month}-{day}")
                    break
            
def word_to_number(month, months):
    for i in range(len(months)):
        if month == months[i]:
            return i + 1
        
def pad(item):
    if int(item) < 10:
        return "0" + str(item)
    else:
        return item
main()

#check50 cs50/problems/2022/python/outdated