
'''
shop=[
    ["Iphone",6000],
    ["Mac computer",12000],
    ["小米 watch",500],
    ["lenovo pc",4500],
    ["辣条",2.5],
    ["泡椒鸡爪",13],
    ["老干妈",10],
]
# 第一种：
# #二维列表，一维列表又套一个一维列表
print("欢迎来到大润发购物广场".center(70,"-"))
# #先初始化自己的金钱
while True:
    salary = input("请输入您的初始金钱：")
    if salary.isdigit():#判断输入的字符串能否看成数字
        salary = int(salary)
        print(salary)
        break
    else:
        print("请重新输入您的初始金额！")
# #展示所有商品
# for index,valude in enumerate(shop):
#     print(index," ",valude)
maycart=[]
while True:
    for index,value in enumerate(shop):
        print(index," ",value)
    choice = input("请输入您要买的商品编号：")
    if choice.isdigit():
        choice = int(choice)
        if choice < len(shop):
            if salary >= shop[choice][1]:
                maycart.append(shop[choice])#添加到我的购物车
                salary -= shop[choice][1]
                print("恭喜您，添加成功！您的余额还剩：",salary)
            else:
                print("对不起，您的余额不足，请退出！")
        else:
                print("您输入的商品编号不存在！请重新输入")
    elif choice == 'q' or choice == 'Q':
        print("欢迎下次光临！！！")
        break
    else:
        print("您输入的不合法，请重新输入！！！！")
print("---------------------------Bye-------------------------")

#打印我的小票
for i in mycart:
    pritn(i)
print("您的余额为：",salary)
'''



#有以下一个列表，求其中是5的倍数的和
# a=[1,5,21,30,15,9,30,24]

# sum=0
# index=-1
# for i in a:
#     if i % 5 ==0:
#         sum=sum+i
# print(sum)


a=[1,5,21,30,15,9,30,24]
'''
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            n=a[j]
            a[j]=a[i]
            a[i]=n
'''
#第一种：选择排序
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[j]>a[i]:
#             c=a[j]
#             a[j]=a[i]
#             a[i]=c
# print(a)

#第二种：冒泡排序
for i in range(len(a)):
    for j in range(len(a)-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]

print(a)





































