import unittest
#再创建一个存储sa和deli数据的断言标准的列表的存储模块
from common.data_handle import gener_complete_sa_list,gener_complete_deli_list
import logging
class ftp_test(unittest.TestCase):

    def test_deli(self):
        for i in range(0,4):
            try:
                assert 1==2
            except AssertionError :
                print("wrong")
                raise
    # 这里不改，下面来一个处理二维的sa的testcase
    def test_deli_sample(self):
        # a = [
        #      ['GK30', '2020082s8', 'NE', 'S115977', ' ', ' ' ,' rw21'],
        #      ['SAHD', ' ', '0000', '0000', '     ', '200818', '122744', '00000', '      ', '      ', 'SHARP ']
        #      ]
        a = ['GK30', '2020082s8', 'NE', 'S115977', ' ', ' ' ,' rw21']

        assert_a = [
            ("m", "F"),("n", "F"),("l", "F"),("m", "F"),("m", "T"),("n", "T"),("m", "F")
        ]
        all_params=len(a)
        pass_params=0
        for i in range(0, len(a)):

            # 是否允许为空为第一层

            if a[i].isspace():
                if assert_a[i][1] == "T":
                    pass_params+=1
                else:
                    logging.error("错误，出错行头是:{},该行第{}个字段出错，不能为空，内容：'{}'".format(a[0], i + 1, a[i]))
                continue

            # 判断字符打头是否是空
            if a[i][0] == " ":
                    logging.error("错误,出错行头是：'{}'，第{}个字段出错，首字符不能为空，可能该行有错位内容：'{}'".format(a[0], i + 1, a[i]))
                    continue


            # 判断字符的类型是否正确
            sign = ""
            if a[i].isdigit():
                sign = "n"
            elif a[i].isalpha():
                sign = "l"
            elif a[i].isalnum():
                sign = "m"
            if sign == assert_a[i][0]:
                pass_params += 1
            else:
                logging.error("错误,出错行头是：'{}'，第{}个字段出错，字段类型错误，内容：'{}'".format(a[0], i + 1, a[i]))

        #判断是否所有字段正确，返回一个布尔值，传给testcase做判断
        if all_params == pass_params:
            assert True
        else:
            logging.error("通过字段：{}".format(pass_params))
            logging.error("共有{}个字段，有{}个字段出错".format(all_params ,(all_params-pass_params)))
            assert False
