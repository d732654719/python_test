import unittest,logging,json
from ddt import ddt,data
from Common.excel_handler import do_excel
from Common.do_jsonpath import repl_jsonpth
# from Common.path_config import *
from Common.https_requests import http_requests
from Common.logger import Mylogger

# 获取测试数据
test_data = do_excel().read_data_by_config()

@ddt
class TestHttpRequest(unittest.TestCase):
    @data(*test_data)
    def test_http_requests(self, data):
        # 全局变量传递接口间参数
        global global_data
        global_data = {}

        logging.info("正在执行：第{}条用例，".format(data["用例编号"]))
        logging.info("替换前请求地址：{0},替换前请求参数：{1},".format(data["接口地址"],data["请求参数"]))
        logging.info("替换前请求文件参数：{0}，请求头：{1}".format(data["文件参数"],data["请求头"]))
        method = data["请求方式"]
        url = repl_jsonpth(data["接口地址"], data["全局变量"])
        params = eval(repl_jsonpth(data["请求参数"], data["全局变量"]))
        header = eval(repl_jsonpth(data["请求头"], data["全局变量"]))
        file_param = eval(repl_jsonpth(data["文件参数"], data["全局变量"]))

        logging.info("替换后请求地址：{0},请求参数：{1},".format(url, params))
        logging.info("替换后请求文件参数：{0}，请求头：{1}".format(file_param, header))

        response = http_requests(method, url, header, params, file_param).json()
        logging.info("响应结果是：{}".format(response))
        # 替换全局变量
        if data['全局变量']:
            result = repl_jsonpth(data["全局变量"], response)

            global_data.update(eval(result))
            logging.info("全局变量:{}".format(global_data))
        # 替换断言表达式中的实际结果
        real_assert_exp = repl_jsonpth(json.dumps(data["断言"]), response)
        logging.info("断言表达式为：{}".format(real_assert_exp))
        # 断言
        try:
            for i in real_assert_exp:
                self.assertTrue(i)
        except AssertionError as e:
            logging.error("断言错误，实际结果与预期结果不符")
            raise e
