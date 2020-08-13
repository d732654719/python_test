import unittest
import HTMLTestRunnerNew
from Common.path_config import *
from Common.test_http_requests import TestHttpRequest
from Common.excel_handler import do_excel

conf_html = do_excel().read_sheet("配置")[0]
title = conf_html["测试报告标题"]
des = conf_html["测试报告描述"]
tester = conf_html["测试人员"]

suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTests(loader.loadTestsFromTestCase(TestHttpRequest))

with open(report_path, "wb+") as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file, title=title, description=des, tester=tester)
    runner.run(suite)

