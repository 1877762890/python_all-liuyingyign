class OldPhone:
    __phoneNumber=""
    __vioce=""
    __brand=""

    def __int__(self,phoneNumber,vioce,brand):
        self.__phoneNumber=phoneNumber
        self.__vioce=vioce
        self.__brand=brand

    def setPhoneNumber(self,phoneNumber):
        self.__phoneNumber=phoneNumber
    def getPhoneNumber(self):
        return self.__phoneNumber

    def setBrand(self,brand):
        self.__brand=brand
    def getBrand(self):
        return self.__brand

    def call(self,number):
        print(self.__phoneNumber,"正在给",number,"打电话")

class NewPhone(OldPhone):
    __place=""
    __picture=""
    __ps=""

    def __init__(self,phoneNumber,vioce,brand,place,picture,ps):
        super().__int__(phoneNumber,vioce,brand)
        self.__place=place
        self.__picture=picture
        self.__ps=ps

    def setPlace(self,place):
        self.__place=place
    def getPlace(self):
        return self.__place

    def setPicture(self,picture):
        self.__picture=picture
    def getPicture(self):
        return self.__picture

    def setPs(self,ps):
        self.__ps=ps
    def getPs(self):
        return self.__ps

    def call(self,number):
        print("正在给",number,"打电话")

    def Introduce(self):
        print("品牌为：",self.getBrand(),"的手机很好用")


phone=NewPhone("15538183791","月亮之上","诺基亚","河南","野猪佩奇","小黑来电")

phone.ps="小黑来电"
phone.call("15824700631")
phone.Introduce()









