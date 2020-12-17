#for循环 九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j,"x",i,"=",(i*j),"\t",end="")
#     print()

#1~10 的和
# sum=0
# for i in range(1,11):
#     sum=sum+i
# print(sum)



#剥离100~999之间的数，并判断这些数是否是水仙数
#123 = 1*1*1 + 2*2*2 + 3*3*3
 #157 是不是水仙花数！
# for a in range(100,1000):
#      b = a // 100
#      s = a // 10 % 10
#      g = a % 10
#      if pow(g,3) + pow(b,3) + pow(s,3) == a:
#          print(a,"是水仙花数！")


#次方的三种输入:
#例如：g的三次方
# g*g*g
# pow(g,3)
# g**3


'''
sum=0
a=1 #表示阶乘
for i in range(1,21):
    a=a*i
    sum=sum+a
print(sum)
'''

max=0
sum=0

for i in range(10):
    num=int(input("请输入数据："))
    if num>max:
        max=num
    sum=sum+num
print("最大值为：",max,"和为：",sum,"平均值为：",(sum/10))