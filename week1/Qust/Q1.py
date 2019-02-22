# .用python语句判断所输入的手机号，是否正确
# 要对手机号的号段进行判断，号段任意给出6个作为模拟号段即可
# .判断手机号码是否是由数字组成的
list = [185,137,178,151,153,136]
print("请输入你的手机号")
phone = input()
bool = False
try:
    int(phone)
    if(len(phone)==11):
        head = phone[0:3]
        for i in list:
            if(int(head)==(i)):
                bool = True
        if(bool):
            print("有效手机号")
        else:
            print("无效手机号")
    else:
        print("无效手机号")
except ValueError:
    print("输入的不是手机号")


