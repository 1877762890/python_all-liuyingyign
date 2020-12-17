class Student:
    __name=None
    __age=None

    def __init__(self,n,a):
        self.__name=n
        self.__age=a

    def setName(self,n):
        self.__name=n
    def getName(self):
        return self.__name

    def setAge(self,a):
        self.__age=a
    def getAge(self):
        return self.__age

    def introduce(self):
        print("大家好，我叫",s.getName(),"今年",s.getAge(),"岁了")
    def compare(self):
        if s.getAge()>p.getAge():
            print("我比同桌大",s.getAge()-p.getAge(),"岁！")
        elif s.getAge()<p.getAge():
            print("我比同桌小",p.getAge()-s.getAge(),"岁！")
        else:
            print("我和同桌一样大！")


s=Student("刘营营",18)
p=Student("刘小黑",20)
s.introduce()
s.compare()














