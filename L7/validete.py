import re
email = input("What's your email? ").strip()

#首先排查特征字符
#然后将字段区分为username和domain
#特征字符可分为单个和多个。一直到这里还在用str的方法

'''rname, domain = email.split("@")
if username and domain.endswith(".edu"):
    print("Valid")
else:
    print("Invalid")'''

#然后就引出了python自带函数re
#补充检索式一样的东西（怎么也叫pattern）
#.的歧义及处理


#if re.search(".@.", email):
#note中是.+@.+, 没有+会怎么样，至少对正常邮箱检测是可以的。 问了deep seek，好像不会怎样
#对多@情况，引入补集概念，对空格情况，引入首尾检测
#if re.search(r"^[^@]+@[^@]+\.edu$", email):

#讨论其他字符:0-9a-zA-Z, 
#ignorecase的使用
if re.search(r"^(\w+\.)?\w+@\w+(\w+\.)?\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")