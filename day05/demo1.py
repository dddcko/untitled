# 通过用户输入数字，计算阶乘。
a = int(input("请输入一个数字:"))
sum = 1
for i in range(a):#遍历从1到该数
    sum *= (i+1)# 用sum记录1到这个数的阶乘
print(a,"的阶乘为:",sum)#输出