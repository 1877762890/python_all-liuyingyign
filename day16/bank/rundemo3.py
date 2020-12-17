import unittest
import os
from HTMLTestRunner import HTMLTestRunner
#创建测试集
suite=unittest.TestSuite()
#获取加载器
loader=unittest.defaultTestLoader
#寻找匹配的用例
cases=loader.discover(os.getcwd() + "\\testcase2",pattern="Test*.py")
#添加到测试集里
suite.addTest(cases)

with open("银行转账测试报告.html","w+",encoding="utf-8") as f:
    runner=HTMLTestRunner.HTMLTestRunner(
        stream=f,
        verbosity=1,
        title="银行转账测试报告",
        description="这是第三次迭代测试"
    )
    runner.run(suite)

