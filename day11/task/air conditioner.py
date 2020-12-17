
class Airconditioner:
    __brand=None
    __price=None

    def __init__(self,b,p):
        self.__brand=b
        self.__price=p

    def setBrand(self,b):
        self.__brand=b
    def getBrand(self):
        return self.__brand

    def setPrice(self,p):
        self.__price=p
    def getPrice(self):
        return self.__price

c=Airconditioner("格力","3000")
print("空调的品牌是:",c.getBrand(),"空调的价格是：",c.getPrice())

def setOpen(self,o):
    self.__open=o
o="空调开机了..."
print(o)


def setClose(self,fenzhong):
    self.__close=fenzhong
fenzhong=int(input("请输入关机时间"))
print("空调将在",fenzhong,"分钟后自动关闭")




















