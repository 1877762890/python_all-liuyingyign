#原始的
class Dog:
    __color=None
    __speed=None
    __belong=None

    def setColor(self,c):
        self.__color=c
    def getColor(self):
        return self.__color

    def setSpeed(self,s):
        self.__speed=s
    def getSpeed(self):
        return self.__speed

    def setBelong(self,b):
        self.__belong=b
    def getBelong(self):
        return self.__belong

d = Dog()
d.setColor("红色")
d.setBelong("犬科")
d.setSpeed("50km/h")

print(d.getColor(),"颜色",d.getBelong(),"科目",d.getSpeed())







#有参构造函数
class Dog:
    __color=None
    __speed=None
    __belong=None

    def __init__(self,c,b,s):
        self.__color=c
        self.__belong=b
        self.__speed=s
    def setColor(self,c):
        self.__color=c
    def getColor(self):
        return self.__color

    def setSpeed(self,s):
        self.__speed=s
    def getSpeed(self):
        return self.__speed

    def setBelong(self,b):
        self.__belong=b
    def getBelong(self):
        return self.__belong
d=Dog("红色","犬科","50km/h")

print(d.getColor(),"颜色",d.getBelong(),"科目",d.getSpeed())
















