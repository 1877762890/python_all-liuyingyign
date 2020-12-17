class bank(Exception):
    def __init__(self,msg):
        self.__msg=msg

def Qvqian():
    p=int(input("请输入取款金额："))
    i=3000
    if p<=i:
        print("取款成功！您的余额为：",i-p)
    else:
        raise bank("余额不足异常！")
Qvqian()

