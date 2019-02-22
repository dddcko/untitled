# 判断101-200之间有多少个素数，并输出所有素数。
# 程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，
# 如果能被整除，则表明此数不是素数，反之是素数。
list = []
for i in range(101,200):#遍历101-200
    bool = True   #定义一个布尔类型的变量，方便判断
    for j in range(2,i): #遍历2到这个数，用这个数循环%小于自己的所有正整数
        if i%j==0:#判断能不能被整除，如果整除了，bool值变成false
            bool = False
    if(bool):#判断bool的值，如果是true 则该数为质数，加入到list中，如果是false，则不是质数，跳过添加直接进行下次循环
        list.append(i)
#  按题目要求打印结果
print(list)
print("101-200之间的素数个数为:",len(list))