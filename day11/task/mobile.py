
class User:
    __username=None
    __sex=None
    __age=None
    __credit=None
    __brandname=None
    __capacity=None
    __screensize=None
    __standbytime=None
    __integral=None
    def __init__(self,username,sex,age,credit,brandname,capacity,screensize,standbytime,integral):
        self.__username=username
        self.__sex=sex
        self.__age=age
        self.__credit=credit
        self.__brandname=brandname
        self.__capacity=capacity
        self.__screensize=screensize
        self.__standbytime=standbytime
        self.__integral=integral
    def setUsername(self,username):
        self.__username=username
    def getUsername(self):
        return self.__username

    def setSex(self,sex):
        self.__sex=sex
    def getSex(self):
        return self.__sex

    def setAge(self,age):
        self.__age=age
    def getAge(self):
        return self.__age

    def setCredit(self,credit):
        self.__credit=credit
    def getCredit(self):
        return self.__credit

    def setBrandname(self,brandname):
        self.__brandname=brandname
    def getBrandname(self):
        return self.__brandname

    def setCapacity(self,capacity):
        self.__capacity=capacity
    def getCapacity(self):
        return self.__capacity

    def setScreensize(self,screensize):
        self.__screensize=screensize
    def getScreensize(self):
        return self.__screensize

    def setStandbytime(self,standbytime):
        self.__standbytime=standbytime
    def getStandbytime(self):
        return self.__standbytime

    def setIntegral(self,integral):
        self.__integral=integral
    def getIntegral(self):
        return self.__integral

    def introduce(self):
        print("我的姓名",n.__username(),"性别为",n.__sex(),"年龄为",n.__age(),"剩余话费",n.__credit(),"手机品牌为",n.__brandname(),"手机电池容量",n.__capacity(),"手机屏幕大小",n.__screensize(),"最大待机时长",n.__standbytime(),"所拥有的积分为",n.__integral())


    def text(self,msq): #发短信
        print(msq)

    def call(self):
        y=input("请输入要打的电话号码：")
        z=int(input("请输入要打的时间长度："))
        if len(y)==None:
            print("电话号码不能为空")
        elif n.__credit<1:
            print("话费余额不足，请充值！")
        else:
            if 0<z<10:
                n.__credit-=z*1
                n.__integral-=z*15
            elif 10<z<20:
                n.__credit-=z*0.8
                n.__integral-=z*39
            else:
                n.__credit-=z*0.65



n=User("刘营营","女",20,5,"小米","3350mAh(typ)","6.26英寸","8小时",100)
n.introduce()
n.text("王府街约火锅！！")
n.call()


