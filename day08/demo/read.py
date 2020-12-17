
f=open("123.jpg", "rb") #读取
w=open("美女.jpg", "wb") #写入

#读取一个图片
data=f.read()
#江都区数据写入到另一个文件中
w.write(data)
#关闭读取和写入资源
f.close()
w.close()
