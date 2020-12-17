# string="this is a dog,that is a monkey!"
# #将字符串转换成列表
# li = list(string)
#
# for i in range(0,len(li)):
#     count=0 #计数器
#     #排重
#     flag=True #开关置为开
#     for k in range(0,i):
#         if li[k] == li[i]:
#             flag=False #一旦发现相同字符，开关置位关闭
#             break
#
#     if flag == False:#判断开关是否是关闭状态，便于判断是否发现是否统计过
#         continue #终止循环，继续下一轮循环
#         #统计
#     for j in range(0,len(li)):
#         if li[i] == li[j]:
#             count+=1
#     print(li[i],"出现了",count,"次!")

#身份运算符 in   not in




'''
方法：函数
def  方法名():
    方法体
好处：一本万利，写一次，能多次使用
'''
# def sum(a,b):#申明一个方法，能接受两个数，并对接受的数据进行求和，然后使用return进行返回
#     print("已登录火星")
#     c=a+b
#     print("任务完成，准备返回地球")
#     return  c
# print("准备登陆火星....")
# s=sum(1,2)
# print("返回成功！")
# print(s)



#有下列列表，请编程实现列表的数据翻转（京东金融的测试开发笔试题）
#List = [1,2,3,4,5,6,7,8,9]
#实现效果：list = [9,8,7,6,5,4,3,2,1]

list=[1,2,3,4,5,6,7,8,9]

for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[j] > list[i]:
            list[j],list[i]=list[i],list[j]
print("list:",list)







#请编程统计列表中的每个数字出现的次数(百度初级测试开发笔试题)
'''
list = [1,4,7,5,82,1,3,4,5,9,7,6,1,10]

for index,ch in enumerate(list):
    if ch in list[:index]:
        continue
    print(ch,"出现了",list.count(ch),"次")

'''
#使用字典的方式来存： key:value    数字:次数
# li=[1, 4, 7, 5, 82, 1, 3, 4, 5, 9, 7, 6, 1, 10]
# d={}
# for i in li:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# print(d)



# 编程实现列表的折线输出(美团笔试题)
# a = [
# 	[1,   2,   3 ,  4],
# 	[5,   6,   7 ,  8],
# 	[9,   10 ,  11,  12],
# 	[13,  14 ,  15,  16]
# ]
# 实现输出：4,3,8,2,7,12,1,6,11,16,5,10,15,9,14,13
#    姓名    年龄  性别  编号 任职公司 薪资 部门编号

'''
names=[
    ["何登勇","56","男","106","IBM",500,"50"],
    ["曹冬雪","19","女","230","微软",501,"60"],
    ["刘营营","19","女","210","Oracle",600,"60"],
    ["李汉聪","45","男","230","Tencent",700,"10"]
]
'''
#统计每个人的平均薪资
'''
sum=0
n=0
for i in range(len(names)):
    sum=sum+names[i][5]
    n=sum/len(names)
print(n)
'''

#统计每个人的平均年龄
'''
sum1=0
m=0
for j in range(len(names)):
    sum1=sum1+int(names[j][1])
    m=sum1/len(names)
print(m)

'''


#公司新来一个员工，张佳伟，45，男，220，alibaba，500,30，添加到列表中
'''
names.append(["张佳伟","45","男","220","alibaba",500,"30"])
print(names)
'''


#统计公司男女人数
'''
for i in range(0,len(names)):
    count=0
    flag=True
    for k in range(0,i):
        if names[k][2]==names[i][2]:
            flag=False
            break
    if flag==False:
        continue
    for j in range(0,len(names)):
        if names[i][2]==names[j][2]:
            count+=1
    print(names[i][2],"出现了",count,"次！")

'''
# for i in range(len(names)):
#     man=0
#     woman=0
#     for j in range(len(names)):
#         if names[i][2]==names[j][2]:
#             man+=1
#         if names [i][2]!=names[j][2]:
#             woman+=1
# print("男人出现：",man,"次","女人出现：",woman,"次")

#每个部门的人数
'''
for i in range(0,len(names)):
    count=0
    flag=True
    for k in range(0,i):
        if names[k][6]==names[i][6]:
            flag=False
            break
    if flag==False:
        continue
    for j in range(0,len(names)):
        if names[i][6]==names[j][6]:
            count+=1
    print(names[i][6],"部门有",count,"人！")

'''
'''
a=[
    [10,14,9,15],
	[7,4,8,10],
	[6,8,4,9],
	[8,51,10,23]
]
max=0
least=0
for i in range(0,len(a)):
    if a[i]>max:
        max=a[i]
for j in range(0,len(a)):
    if a[j]<least:
        least=a[j]
print("最大为：",max,"最小为：",least)

'''



































































































