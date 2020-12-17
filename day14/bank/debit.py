import unittest
from day14.bank.bankdemo import bank_takeMoney
from day14.bank.bankdemo import findByAccount
from day14.bank.bankdemo import bank_saveMoney



class TestBank1(unittest.TestCase):
    def testBank_transformMoney(self):
        outputaccount=165146145
        inputaccount=9842894892
        outputpassword="123456"
        outputmoney="654321"



        status = bank_takeMoney(outputaccount, outputpassword, outputmoney)
        if status == 1:
            return status
        elif status == 2:
            return status
        elif status == 3:
            return status

        if inputaccount != None and findByAccount(inputaccount) != None:
            bank_saveMoney(inputaccount, outputmoney)
            return 0
        else:
            return 1


