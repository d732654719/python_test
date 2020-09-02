import unittest
import HTMLTestRunnerNew
import os
from testCase.testCase import ftp_test

project_path = os.path.split(os.path.realpath(__file__),)[0]
report_path=os.path.join(project_path, "report_html", "report.html")

title = "SHARP出向接口测试"
des = "出向接口包含'sa_from_jusda'和'纳品'"
tester = "邓畅"

suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTests(loader.loadTestsFromTestCase(ftp_test))

with open(report_path, "wb+") as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file, title=title, description=des, tester=tester)
    runner.run(suite)