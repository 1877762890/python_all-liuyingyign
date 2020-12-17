
class cook:
    __name=""
    __age=""

    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    def setName(self,name):
        self.__name=name
    def getName(self):
        return self.__name

    def setAge(self,age):
        self.__age=age
    def getAge(self):
        return self.__age

def Introduce(self):
   print("我叫",self.__name,"我今年",self.__age,"岁")


    # def zhengfan(self):
    #     __rice=""
    #     __water=""
    #
    # def setRice(self,rice):
    #     self.__rice=rice
    # def setWater(self,water):
    #     self.__water=water
    #
    # def zuo(self):
    #     print("先倒入米",self.__rice,"再倒入水",self.__water)











c=cook("张三",30)
# c.rice="100克"
# c.water="500ml"
# c.zhengfan()





