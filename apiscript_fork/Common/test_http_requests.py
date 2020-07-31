import unittest,logging,json
from ddt import ddt,data
from Common.excel_handler import do_excel
from Common.do_jsonpath import repl_jsonpth
from Common.path_config import *
from Common.https_requests import http_requests

# 获取测试数据
test_data = do_excel().read_config()

@ddt
class TestHttpRequest(unittest.TestCase):
    @data(*test_data)
    def test_http_requests(self, data):
        logging.info("正在执行：{}条用例，".format(data["用例编号"]))
        logging.info("替换前请求地址：{0},替换前请求参数：{1},".format(data["接口地址"],data["请求参数"]))
        logging.info("替换前请求文件参数：{0}，请求头：{1}".format(data["文件参数"],data["请求头"]))
        method = data["请求方式"]
        url = repl_jsonpth(data["接口地址"], data["关联变量"])
        params = repl_jsonpth(data["请求参数"], data["关联变量"])
        header = repl_jsonpth(data["请求头"], data["关联变量"])
        file_param = repl_jsonpth(data["文件参数"], data["关联变量"])

        logging.info("替换后请求地址：{0},请求参数：{1},".format(url, params))
        logging.info("替换后请求文件参数：{0}，请求头：{1}".format(file_param, header))

        response = http_requests(method, url, header, params,file_param)
        logging.info("响应结果是：{}".format(response))
