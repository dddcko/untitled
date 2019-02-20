# print("请输入第一个人的生日(格式例如20180101):")
# a = int(input())
# print("请输入第二个人的生日(格式例如20180101):")0
# b = int(input())
# if(a>b):
#     print("b的年龄大")
# elif(b>a):
#     print("a的年龄大")
# else:
#     print("a与b的年龄相等")

import random
A = []
for i in range(10):
    a = random.choice(range(10))
    A.append(a)
print(A)
b = random.choice(range(10))
if b in A:
    print(b)
    print("有")
else:
    print(b)
    print("没有")