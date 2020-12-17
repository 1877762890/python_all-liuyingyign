class student:
    __studentNumber=None
    __name=None
    __age=None
    __sex=None
    __height=None
    __weight=None
    __score=None
    __address=None
    __phoneNumber=None

    def __init__(self,studentNumber,name,age,sex,height,weight,score,address,phoneNumber):
        self.__studentNumber=studentNumber
        self.__name=name
        self.__age=age
        self.__sex=sex
        self.__height=height


    def setStudentNumber(self,studentNumber):
        self.__studentNumber=studentNumber
    def getStudentNumber(self):
        return self.__studentNumber













