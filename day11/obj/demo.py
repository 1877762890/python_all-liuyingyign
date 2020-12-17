'''
   1.类：（类名首字母必须大写，第二个单词开始首字母大写）
       属性
       行为（功能）
   2.对象
       c=Car()
       句柄=类名
   3.封装：
       3.1将属性进行私有化
          将属性前面加上__
       3.2提供方法简介赋值
   类对象：
       1.属性封装
       2.提供setxxx/getxxx
       3.提供无参、有惨构造函数
'''

class Person:
    __username=""
    __age=None
    def setUsername(self,u):
        self.__username=u
    def setAge(self,a):
        if a == None:
            print("输入非法！")
        elif a>120 or a<0:
            print("输入非法！")
        else:
            self.__age=a
    def show(self):
        print("我叫",self.__username,"我的年龄为：",self.__age)

p=Person()

p.setUsername("刘营营")
p.setAge(18)
p.show()














