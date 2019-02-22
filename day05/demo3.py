# 将一个列表的数据复制到另一个列表中，并反向排序输出

import random #导入随机包
list = [] #定义一个列表
for i in range(10): #循环10次，往列表里添加10个随机数字
    a = random.randint(1,100) #随机一个数并赋值给a
    list.append(a)  #将a添加到list中
print("正序输结果是:",list)   #输出正序
list.reverse()  #调用反向排序方法
print("反向排序结果是:",list) #输出反序

