# 新建一个文件夹
f = open('test.txt','w')
f.close() # 关闭f流
# 使用write向文件写入数据
f = open('test.txt','w')
f.write('hello world!!!')
f.close() #写入后，关闭f流
# 读数据
f = open('test2.txt','w')
f.close()#关闭f流
#开始打印文件内容
f = open('test.txt','r')
str = f.read(15) #将读到的文件内容赋值给str
print(str) #打印str字符串
f.close()#关闭f流
#写到第二个文件中
f = open('test2.txt','w')# 创建第二个文件夹
f.write(str) # 直接将str 写入文件中
f.close()#关闭f流

