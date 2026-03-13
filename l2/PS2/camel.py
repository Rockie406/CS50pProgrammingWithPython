def main():
    #input the users name
    camel_name = input("input a camel name: ")
    camel_name_comma = ",".join(camel_name)
    camel_list = []
    #print(camel_list)

    for letter in camel_name:
        if letter.isupper():
            camel_list.append("_" + letter.lower())
        else:
            camel_list.append(letter)
    for element in camel_list:
        print(element, end="")


main()

''' #str to list
    #遍历全部元素
    for element in camel_list:
        #定位大写字母
        if element.isupper():
            #前置","改"_"，死循环
            iindex = [].append(index)
            index += 1
            print(index)
    print(iindex)
    #删去","
    #list to str'''
#check50 cs50/problems/2022/python/camel
#submit50 cs50/problems/2022/python/camel