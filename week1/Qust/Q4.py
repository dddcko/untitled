# 随机生成一个包含1000个字母的字符串，然后统计该字符串中每个字母的数量，
# 并输出结果（要求结果以字典方式存储）
import random
str =  'abcd'
str1 = ''
for i in range(1000):
    str1 += random.choice(str)
dict = {}
for i in str1:
    key = dict.get(i)
    if(key == None):
        dict[i] = 1
    else:
        dict[i] += 1
print(dict)