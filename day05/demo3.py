# 将一个列表的数据复制到另一个列表中，并反向排序输出
import random
list = []
list1 = []
for i in range(10):
    a = random.randint(1,100)
    list.append(a)
print("正序输结果是:",list)
for j in range(-9,1):
    b = (j**2)**(1/2)
    b = int(b)
    list1.append(list[b])
print("反向排序结果是:",list1)

