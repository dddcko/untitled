# 通过用户输入数字，计算阶乘。
a = int(input("请输入一个数字:"))
sum = 1
for i in range(a):
    sum *= (i+1)
print(a,"的阶乘为:",sum)