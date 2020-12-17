import  datetime
from day11.bank.tools import tools
class User:
    '''
    账号（int）、姓名（Str）、密码（6位数字）、地址、存款余额（double）、注册时间（date）、开户行（银行的名称（String））
    '''
    __account=None #系统自动产生的，不需要提供set方法，可以提供get方法
    __username=None
    __password=None
    __address=None
    __money=None
    __reg_date=None #不需要提供set方法，可以提供get方法
    __bankname=None #不需要提供set方法，可以提供get方法，应该去银行那边取数据
    def __init__(self,username,password,address,money):
        self.__username=username
        self.__password=password
        self.__address=address
        self.__money=money
        self.__account=tools().getRandom() #获取随机码
        self.__bankname="中国工商银行昌平支行"
        self.__reg_date=datetime

    def getAccount(self):
        return self.__account
    def setUsername(self,username):
        self.__username=username
    def getUsername(self):
        return self.__username

    def setPassword(self,password):
        self.__password=password
    def getPassword(self):
        return self.__password

    def setAddress(self,address):
        self.__address=address
    def getAddress(self):
        return self.__address

    def setMoney(self,money):
        self.__money=money
    def getMoney(self):
        return self.__money

    def getReg_date(self):
        return self.__reg_date

    def getBankname(self):
         return self.__bankname

u=User("刘营营","123456","河南省商丘市021街道100号","10000")

print("我叫:",u.getUsername(),"我的密码是:",u.getPassword(),"我的地址是:",u.getAddress(),"我的余额为:",u.getMoney())








