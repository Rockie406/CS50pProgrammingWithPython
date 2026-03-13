# Then output the user’s grocery list in all uppercase, sorted alphabetically by item,
#  prefixing each line with the number of times the user inputted that item. 
# No need to pluralize the items. Treat the user’s input case-insensitively.

def main():

    dict = {}
    while True:
        #1.输入+计数
        try:
            item = input().upper()
        except EOFError:
            break
        else:
            #2.1 计数
            try:
                dict[item]
            except KeyError:
                dict[item] = 1
            else:
                dict[item] += 1
    how_much(sort(dict))
        #how_much(sort(dict))若直接键入ctrl z，会因为new_dict空值引发error

#2 排序：前后比较大小，循环len(dict)次
def sort(dict):
    key = list(dict.keys())#能找到keys，但好像带有其他字符。用list转化
    value = list(dict.values())
    cls = 1
    while cls <= len(dict):
        for i in range(len(dict) - 1):
            if key[i] <= key[i + 1]:
                pass
            else:
                middle_key = key[i + 1]
                middle_value = value[i + 1]
                key[i + 1] = key[i]
                value[i + 1] = value[i]
                key[i] = middle_key
                value[i] = middle_value
        cls += 1
    new_dict = {}#若缩进，会导致how_much(sort(dict))直接键入ctrl z时因为called循环被跳过，new_dict空值引发error
    for i in range(len(dict)):#i为什么有一个初始的0值，因为range是左闭右开
        new_dict[key[i]] = value[i]
    return new_dict

#3 输出
def how_much(dict):
    for item in dict:
        print(dict[item], item)               

                
main()


        
