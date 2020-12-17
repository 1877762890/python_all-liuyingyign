#登录系统
# f=open("n.txt","r+",encoding="utf-8")
# data=f.readlines()
# for i in data:
#     line=i.split(",")
#     n[line[0]]=line[1].replace("\n","")
# print(n)
#
# name=input("请输入您的用户名：")
# password=input("请输入您的密码：")
#
# if name in n:
#     if password==n[name]:
#         print("登录成功")
#     else:
#         print("输入密码错误")
# else:
#     print("该用户不存在，系统报错")

'''
f=open("scores.txt","r+",encoding="utf-8")
lines=f.readlines()
f.close()
results=[]
for line  in lines:
    data=line.split()
    print(data)
    sum=0
    for score in data[1:]:
        sum+=int(score)
    result="%s:%d\n"%(data[0],sum)
    print(result)
    results.append(result)
output=open("result.txt","w")
output.writelines(results)
output.close()
'''

'''
f=open("scores.txt","r+",encoding="utf-8")
dic={}
lines=f.readlines()
for line in lines:
    li=line.replace("\n","").split(" ")
    name=li[0]
    scores=li[1:]
    dic[name]=sum([int(i) for i in scores])
print(dic)
'''


f=open("baidu_x_system.log","r+",encoding="utf-8")
dic={}
lines=f.readlines()
for line in lines:
    ip=line.split(" ")[0]
    if ip in dic:
        dic[ip]=dic[ip]+1
    else:
        dic[ip]=1
print(dic)












