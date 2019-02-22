# 编写程序，生成一个包含50个随机整数的列表，随机整数的范围是从-10到10
# 然后将列表中所有的正数存为一个新的子列表，负数存为另一个新的子列表。
import random
list = []
for i in range(50):
    a = random.choice(range(-10,11))
    list.append(a)
print("list长度:",len(list))
zheng = []
fu = []
for i in list:
    if i>0:
        zheng.append(i)
    elif i<0:
        fu.append(i)
print("正数:",zheng)
print("负数:",fu)
