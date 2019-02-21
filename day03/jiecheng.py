# 2.二 输入一个数求1！+2！+3！+4！+n！=？
a = int(input("请输入一个数:"))
# suma记录总和
suma = 0
for x in range(1,a+1):# 遍历输入的未知数的长度
    # sum用来记录每段的阶乘
    sum = 1
    # 开始计算每段的阶乘
    for i in range(1,x+1):# 开始计算每段长度的积
        sum *= i
    print("sum:",sum)
    # 用suma在循环内加上每段阶乘的结果,并打印输出
    suma += sum
print("1！+2！+3！+4！+a！:",suma)