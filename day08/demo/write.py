'''
1、写入到文件：a.txt
2、写入的数据：”万能的测试开发“

'''
# 1、打开文件，并获取文件句柄（把柄）
f=open("a.txt", "w+", encoding="utf-8")

#2、写入数据

f.write("窗前明月光，\n")#用c语言底层资源
f.write("梦见喝鸡汤；\n")
f.write("抬头吃鸡腿，\n")
f.write("低头刘口水。\n")
#3、关闭资源
f.close()