##理不全逻辑关系，修改时多次盲人摸象，东西墙边拆边补，有点痛苦
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



   #整理这些异常，抽象到编程领域对应的术语，为日后所用
   #总体是一个由表及里，检查格式再处理的思路
   #0 输入、去多余字符
   #1 格式检查：分隔符的数量、位置
   #2 元素区分
   #3 元素格式检查、处理
   #3.1 day
   #3.2 month
   #一些小细节：留意变量的type一致
   #if的嵌套是不是说明了某种逻辑的包含关系?嗯，if嵌套本质是and



    while True:  
        #error_time用于记录不至于报错的异常，在最终输出段制止print+break，达到reject prompt的效果。
        #本质来说是有问题的。毕竟会放任异常流动，一是逻辑上不好理，预期应该集中处理这种逻辑问题
        #二是异常值算了也卡在输出，浪费算力
        error_time = 0  
        date = input("Date: ").strip()#可以搞个“纯净input”的函数了

        #1 格式检查：分隔符的数量、位置
        #格式管控： 月、日有<10和>10两种情况，对应不同的month、day宽度，因此str最前面的定位，
        #或者说对month、day之间的分隔符判定是困难的
        #考虑一：保证分隔符数量一致
        #考虑二：因为year位数不变，根据year前的分隔符可以判断一部分格式和输入（如年份）异常
        if (date.count("/") == 2 and date[-5] == "/") or (date.count(", ") == 1 and date.count(" ") == 2 and date[-5] == " " and date[-6] == ","):
            #2 元素区分
            try:
                month, day, year = date.split("/")
            #if September 8, 1636  inputed
            except ValueError:
                monthday, year = date.split(", ")
                month, day = monthday.split(" ")
            #3 day判定处理
            #避免字母月份错打到day，以及day > 31的情况
            if day.isnumeric() and int(day) <= 31:
                day = pad(day) #return为什么没有break外层循环,因为return不是所有情况都发生
                #4 month判定处理
                #两种格式下month的转换
                if (month.isalpha() and not date.find(", ") == -1):
                    month = pad(word_to_number(month, months))
                elif (month.isnumeric() and not date.find("/") == -1):
                    month = pad(month)
                #5 print
                if month.isnumeric() and int(month) <= 12:
                    print(f"{year}-{month}-{day}")
                    break
    
def word_to_number(month, months):
    for i in range(len(months)):
        if month == months[i]:
            return str(i + 1)
        
def pad(item):
    if int(item) < 10:
        return "0" + str(item)
    else:
        return item
main()

#check50 cs50/problems/2022/python/outdated