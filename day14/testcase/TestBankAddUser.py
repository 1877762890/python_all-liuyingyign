import unittest
from day14.bank.bankdemo import bank_addUser
'''
   1.搞清楚那些是要测的业务逻辑部分。
   2.写核心代码
   3.业务:
         用户满了：3
         已经存在：2
         开户成功：1
         username,password,country,province,street,door,money
'''



class TestBankAddUser(unittest.TestCase):

    def testAddUser(self):
        username="jason"
        password="admin"
        country="中国"
        province="安徽省"
        street="幸福大道"
        door="s001"
        money=1000


        status=1 #期望结果
        #实际结果
        s=bank_addUser(username,password,country,province,street,door,money)

        #断言
        self.assertEqual(status,s)

    def testAddUser1(self):
        status=3 #期望值
        password="admin"
        country="中国"
        province="河南"
        street="幸福大道"
        door="s001"
        money=4000
        # 先添加100用户
        for i in range(100):
            username="jason"+str(i)
            #实际结果
            bank_addUser(username,password,country,province,street,door,money)