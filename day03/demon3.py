''''# name=input("请输入姓名:")
# id=input("请输入身份证号:")
# age=int(input("请输入年龄:"))
# sex=input("请输入性别:")
# height=int(input("请输入身高:"))
# weight=int(input("请输入体重:"))
#
# info='''
# --------------个人信息--------------
# 姓名:{name}
# 年龄:{age}
# 身份证:{id}
# 身高:{height}
# 体重:{weight}
# 性别:{sex}
# --------------------------------------
# '''
# print(info.format(name=name,age=age,id=id,height=height,weight=weight,sex=sex))


# 使用random模块，产生 50~150之间的数
# import random
# #使用random模块：50~150
# num=int(random.random()*100+50)
# print(num)


# 编程实现99乘法表的倒叙打印
# num = int(input("请输入您要的层数"))
# i = 9
# while i <= num and i > 0:
#     print("第",i,"层",end="")
#     j = 1
#     while j <= i:
#         print(j,"X",i,"=",(j*i),"\t",end="")
#         j = j + 1
#     print()
#     i = i - 1

for i in range(9,0,-1):
    for j in range(1,i+1):
        print(j,"x",i,"=",(i*j),"\t",end="")
    print()











#从键盘输入任意三边，判断是否能形成三角形，若可以，则判断形成什么三角形
# a=int(input("请输入第一边:"))
# b=int(input("请输入第二边:"))
# c=int(input("请输入第三边:"))
# while True:
#     if a+b>c and b+c>a and a+c>b:
#         print()
#         break
#     elif a==b and b==c:
#         print("等边三角形")
#         break
#     elif a==b or b==c or a==c:
#         print("等腰三角形")
#         break
#     else:
#         print("普通三角形")
#         break

# a=int(input("请输入第一边:"))
# b=int(input("请输入第二边:"))
# c=int(input("请输入第三边:"))
#
# if(a+b>c) and (a+c>b) and (b+c>a):
#     if a == b == c:
#         print("等边三角形！")
#     elif a==b or b==c or a==c:
#         print("等腰三角形！")
#     elif (a*a+b*b==c*c) or (b*b+c*c==a*a) or (a*a+c*c==b*b):
#         print("直角三角形！")
#     else:
#         print("普通三角形！")
# else:
#     print("不能形成三角形")



#有以下两个数，使用+号实现两个数的调换
# A=56
# B=78
# A=A+B
# B=A-B
# A=A-B
# print(A)
# print(B)


#实现登陆系统的三次密码输入错误锁定功能
# i=0
# while i<3:
#     password = 7410
#     num=int(input("请输入您的密码："))
#     if num != password:
#         print("您输入的密码错误")
#     else:
#         print("您输入的密码正确")
#         break
#     i=i+1
# else:
#     print("密码被冻结")

# name="yingying"
# password="1798"
#
# for i in range(3):
#     n=input("请输入用户名：")
#     p=input("请输入密码：")
#     if n == name and p == password:
#         print("恭喜，登录成功！")
#         break
#     else:
#         print("密码输入失败！")
#         if i == 2:
#             print("三次密码输入错误！系统已锁定，请在30分钟后重新登录！")
#             break






#编程实现下列图形的打印
# i=1
# while i<=7:
#     j=1
#     while j<=7-i:
#         print(" ",end="")
#         j=j+1
#     k=1
#     while k<=i:
#         print("*".center(2),end="")
#         k=k+1
#     i=i+1
#     print()


#一只青蛙掉在井里了，井高20米，青蛙白天网上爬3米，晚上下滑2米，问第几天能出来？
# bai=3
# wan=2
# h=20
# count=0
# high=0
#
# while True:
#     count=count+1
#
#     high=high+3
#     if high>=h:
#         break
#     high=high-2
# print("第",count,"天爬出来！")