import  random
class computer:
    __add=""
    __cut=""
    __ride=""
    __remove=""

    # def __init__(self,add,jian,ride,remove):
    #      self.__add=add
    #      self.__jian=jian
    #      self.__ride=ride
    #      self.__remove=remove
    #
    # def setAdd(self,add):
    #     self.__add=add
    # def getAdd(self):
    #     return self.__add
    #
    # def setCut(self,jian):
    #     self.__jian=jian
    # def getCut(self):
    #     return self.__jian
    #
    # def setRide(self,ride):
    #     self.__ride=ride
    # def getRide(self):
    #     return self.__ride
    #
    # def setRemove(self,remove):
    #     self.__remove=remove
    # def getRemove(self):
    #     return self.__remove


    def add(self,*agrs):
        sum=0
        for i in agrs:
            sum+=i
        print(sum)

    def cut(self,*args):
        cha=args[0] #设定从0角标开始
        for j in args[1:]: #[1:]从1角标开始分割
            cha-=j
        print(cha)

    def ride(self,*args):
        ji=args[0]
        for k in args[1:]:
            ji*=k
        print(ji)

    def remove(self,*args):
        shang=args[0]
        for h in args[1:]:
            shang/=h
        print(shang)






c=computer()
c.add(1,2,3)
c.cut(5,2,1)
c.ride(1,1,3,5)
c.remove(10,5,5)






