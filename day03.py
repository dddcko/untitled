print("请输入第一个人的生日(格式例如20180101):")
a = int(input())
print("请输入第二个人的生日(格式例如20180101):")
b = int(input())
if(a>b):
    print("b的年龄大")
elif(b>a):
    print("a的年龄大")
else:
    print("a与b的年龄相等")

import random
A = []
for i in range(5):
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


import random
list = []
for i in range(5):
    a = random.choice(range(10))
    list.append(a)
print(list)
b = random.choice(range(10))
print(b)
if b in list:
    print("list中含有b")
else:
    print("list中没有b")

# 1.有一列分数序列，2／1，3／2，5／3，8／5。。。求出前20项之和
a = 2
b = 1
c = 0
sum = 0
for i in range(1,21):
    sum += a/b
    print(a/b)
    c = a
    a = a+b
    print("a:",a)
    b = c
    print("b:",b)
print("总和为:",sum)

# 2.二 输入一个数求1！+2！+3！+4！+n！=？
a = int(input("请输入一个数:"))
suma = 0
for x in range(1,a+1):
    sum = 1
    for i in range(1,x+1):
        sum *= i
    print("sum:",sum)
    suma += sum
print("1！+2！+3！+4！+a！:",suma)

# 3.有四个数字1，2，3，4，能组成多少个互不相同的三位数
i = 0
list = []
for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            if(a!=b and a!=b and b!=c):
                sum = (a*100+b*10+c)
                i += 1
                list.append(sum)
print(list)
print("一共有"+str(i)+"种方法")

# 4.实现100-200里面所有的质数字,打印这些质数并且求出个数
a = 100
count = 0
while a <= 200:
    sum = 0
    for i in range(2,a):
        b = a%i
        if(b == 0):
           sum += 1
    if(sum == 0):
        print(a)
        count += 1
    a += 1
print("总数为",count)

# 电脑随机生成1~100随机数，用户输入一个数字，电脑提示用户大或者小，猜错，继续提示；猜对，则程序终止
import random
a = random.choice(range(100))
while True:
    x = int(input("请输入一个1~100的数字:"))
    if(x>a):
        print("小")
    elif(x<a):
        print("大")
    else:
        print("猜对了")
        break

