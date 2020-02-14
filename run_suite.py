# 1. 导包
import unittest
from tools.HTMLTestRunner import HTMLTestRunner
# 2. 组装测试套件
suite = unittest.defaultTestLoader.discover("./scripts",pattern="test*.py")
# 3. 获取报告存储文件流 实例化HTMLTestRunner 调用run执行测试套件
with open("./report/report.html", "wb") as f:
    HTMLTestRunner(stream=f).run(suite)
