'''
name=input("请输入姓名")
id=int(input("请输入身份证号"))
age=int(input("请输入年龄"))
sex=input("请输入性别")
height=int(input("请输入身高"))
weight=int(input("请输入体重"))
print(name,id,age,sex,height,weight)
if age> 18:
    print("可以看电影")
else:
    print("年龄不符合")

'''




stu1=45
stu2=23
print("总和:",(stu1+stu2))

num1=15.3
num2=65.7
num3=30
print("总和:",int(num1+num2+num3))

num1=45
num2=num1
print(num2)