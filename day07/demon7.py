'''
好处：一本万利，一次书写，处处使用。
def 【方法名】（参数列表）：
      方法体
      [return]
    参数列表：
    1、单值传输
    2、*args:元组：能不定量的接受参数
    3、**kwargs:字典
    4、注意：3个参数列表的位置是禁止调换的。
'''
'''
def showInfo(name,age,*args):
    print(name,"------",age)
    for i in args:
        print(i)
showInfo("刘营营",2,"女")

'''
# 就用方法来打印 1~100 以内的1数据：（方法的递归（循环）调用）

i=1
def printNum(i):
    if i <= 100:
        print(i)
        i=i+1
        printNum(i)
printNum(i)

