# 电脑随机生成1~100随机数，用户输入一个数字，电脑提示用户大或者小，猜错，继续提示；猜对，则程序终止
import random # 导入随机包
a = random.randint(1,100)# 随机生成一个1~100的数字
while True: # 猜错重新猜，猜不出来一直猜，直接无限循环，在循环内进行输入、判断
    x = int(input("请输入一个1~100的数字:"))#在控制台提示输入一个数字
    if(x>a):#开始判断输入的数字是否大于电脑随机的数字
        print("小")
    elif(x<a):#开始判断输入的数字是否小于电脑随机的数字
        print("大")
    else:# 输入的数字等于电脑随机的数字，则输出猜对了
        print("猜对了")
        break # 猜正确了，用break退出while循环，游戏结束

