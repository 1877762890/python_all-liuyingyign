from day13.task.demo5 import AgeException

class Person:
    __age=None

    def setAge(self,age):
        self.__age=age
    def getAge(self):
        return self.__age

    def compare(self,n):
        if self.__age>n.getAge():
            print("设置合理！")
        else:
            raise AgeException("设置非法！")













