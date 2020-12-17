import time
class Animal(object):
    __color=""
    __weight=""
    __age=""

    def __init__(self,color,weight,age):
        self.__color=color
        self.__weight=weight
        self.__age=age

    def setColor(self,color):
        self.__color=color
    def getColor(self):
        return self.__color

    def setWeight(self,weight):
        self.__weight=weight
    def getWeight(self):
        return self.__weight

    def setAge(self,age):
        self.__age=age
    def getAge(self):
        return self.__age

class Dog(Animal):
    __brand=""

    def __init__(self,color,weight,age,brand):
        super().__init__(color,weight,age) #三个属性交给父类进行初始化 对象.方法（）
        self.__brand=brand

    def setBrand(self,brand):
        self.__brand=brand
    def getBrand(self):
        return self.__brand

    def Show(self):
        for i in range(3): #叫的次数，3次
            print("汪",end="")
            time.sleep(1) #叫的间隔时间 1秒
        print("我是",self.getColor(),"的狗",
              "我的体重是",self.getWeight(),"kg",
              "我的最长寿命是",self.getAge(),"年",
              "我是：",self.getBrand())

d=Dog("黄色",10,10,"犬科")
d.Show()




