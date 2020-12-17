def devision(a,b):
    try:
        print(a/b)
        return"除法正常处理！"
    except IndexError as e:
        print("角标异常！")
        return 1
    except ZeroDivisionError as e:
        print("被除数不能为0异常!")
        return 2
    finally:
        print("之星最终代码块！")
        return 3
s=devision(9,3)
print(s)

