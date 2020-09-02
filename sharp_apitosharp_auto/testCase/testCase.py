import unittest
# 再创建一个存储sa和deli数据的断言标准的列表的存储模块
from common.data_handle import gener_complete_sa_list,gener_complete_deli_list
import logging
class ftp_test(unittest.TestCase):

    def test_deli_sample(self):
        l = ['GK30', '2020082s8', 'NE', 'S115977  ', ' ', ' rw21', ' ']
        # 处理原生的切割数据，使字符串尾部的空格去掉
        a=[]
        for i in l:
            if i.isspace():
                a.append(i)
            else:
                a.append(i.rstrip())
        assert_a = [
            ("m", "T","GK30"),("n", "T"),("l", "T"),("m", "T"),("m", "F"),("n", "F"),("m", "T")
        ]
        all_params=len(a)
        pass_params=0
        for i in range(0, len(a)):

            # 是否允许为空为第一层
            if a[i].isspace():
                if assert_a[i][1] == "T":
                    logging.error("错误，出错行头是:{},该行第{}个字段出错，不能为空，内容：'{}'".format(a[0], i + 1, a[i]))
                else:
                    pass_params += 1
                continue
            # 判断字符打头是否是空
            if a[i][0] == " " and a[i][-1] != " ":
                    logging.error("错误,出错行头是：'{}'，第{}个字段出错，首字符不能为空，可能该行有错位内容：'{}'".format(a[0], i + 1, a[i]))
                    continue
            # 判断固定值是否正确
            if len(assert_a[i]) == 3:
                if assert_a[i][2] == a[i]:
                    pass_params += 1
                else:
                    logging.error("错误,出错行头是:'{}',该行第{}个字段出错,固定值值出错,内容:'{}'".format(a[0], i + 1, a[i]))
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

        # 判断是否所有字段正确，返回一个布尔值，传给testcase做判断
        if all_params == pass_params:
            assert True
        else:
            logging.error("通过字段：{}".format(pass_params))
            logging.error("共有{}个字段，有{}个字段出错".format(all_params ,(all_params-pass_params)))
            assert False


    def test_sa_sample(self):
        a = [
            ['GK30', '2020082s8', 'NE ', 'S115977', ' ', '123x', ' rw21'],
            ['SAHD', ' ', '0000', ' abuse' ]
        ]
        # 处理原生的切割数据，使字符串尾部的空格去掉
        for i in range(0, len(a)):
            for j in range(0, len(a[i])):
                if a[i][j].isspace():
                    continue
                else:
                    a[i][j] = a[i][j].rstrip()
        # T代表必填
        assert_a = [
            [("m", "T","GK30"),("n", "T"),("l", "T"),("m", "T"),("m", "F"),("n", "F"),("m", "T")],
            [("l", "T"),("n", "T"),("n", "T"),("l", "T")]
        ]
        all_params = 0
        for i in a:
            all_params += len(i)
        pass_params=0
        # 遍历所有字段
        for i in range(0, len(a)):
            for j in range(0,len(a[i])):
                # 是否允许为空为第一个判断

                if a[i][j].isspace():
                    if assert_a[i][j][1] == "T":
                        logging.error("错误,出错行头是:'{}',该行第{}个字段出错,不能为空,内容:'{}'".format(a[i][0], j + 1, a[i][j]))
                    else:
                        pass_params += 1
                    continue
                # 判断字符打头是否是空
                if a[i][j][0] == " " and a[i][j][-1] != " ":
                        logging.error("错误,出错行头是:'{}',第{}个字段出错,字段开头不能为空,可能该行有错位,内容:'{}'".format(a[i][0], j + 1, a[i][j]))
                        continue
                # 判断固定值是否正确
                if len(assert_a[i][j]) == 3:
                    if assert_a[i][j][2] == a[i][j]:
                        pass_params += 1
                    else:
                        logging.error("错误,出错行头是:'{}',该行第{}个字段出错,固定值值出错,内容:'{}'".format(a[i][0], j + 1, a[i][j]))
                    continue

                # 判断字符的类型是否正确
                sign = ""
                if a[i][j].isdigit():
                    sign = "n"
                elif a[i][j].isalpha():
                    sign = "l"
                elif a[i][j].isalnum():
                    sign = "m"
                if sign == assert_a[i][j][0]:
                    pass_params += 1
                else:
                    logging.error("错误,出错行头是:'{}',第{}个字段出错,字段类型错误,内容:'{}'".format(a[i][0], j + 1, a[i][j]))

        # 判断是否所有字段正确，返回一个布尔值，传给testcase做判断
        if all_params == pass_params:
            logging.error("字段全部通过")
            assert True
        else:
            logging.error("通过字段：{}".format(pass_params))
            logging.error("共有{}个字段，有{}个字段出错".format(all_params ,(all_params-pass_params)))
            assert False

    # def test_sa_sample(self,a):
    #     a = [
    #         ['GK30', '2020082s8', 'NE', 'S115977', ' ', ' ', ' rw21'],
    #         ['SAHD', ' ', '0000', ' abuse', ]
    #     ]
    #
    #     assert_a = [
    #         [("m", "F"),("n", "F"),("l", "F"),("m", "F"),("m", "T"),("n", "T"),("m", "F")],
    #         [("m", "F"),("n", "F"),("n", "F"),("l", "F")]
    #     ]
    #     all_params=len(a)
    #     pass_params=0
    #     for i in range(0, len(a)):
    #
    #         # 是否允许为空为第一层
    #
    #         if a[i].isspace():
    #             if assert_a[i][1] == "T":
    #                 pass_params+=1
    #             else:
    #                 logging.error("错误，出错行头是:{},该行第{}个字段出错，不能为空，内容：'{}'".format(a[0], i + 1, a[i]))
    #             continue
    #
    #         # 判断字符打头是否是空
    #         if a[i][0] == " ":
    #                 logging.error("错误,出错行头是：'{}'，第{}个字段出错，首字符不能为空，可能该行有错位内容：'{}'".format(a[0], i + 1, a[i]))
    #                 continue
    #
    #         # 判断字符的类型是否正确
    #         sign = ""
    #         if a[i].isdigit():
    #             sign = "n"
    #         elif a[i].isalpha():
    #             sign = "l"
    #         elif a[i].isalnum():
    #             sign = "m"
    #         if sign == assert_a[i][0]:
    #             pass_params += 1
    #         else:
    #             logging.error("错误,出错行头是：'{}'，第{}个字段出错，字段类型错误，内容：'{}'".format(a[0], i + 1, a[i]))
    #
    #     # 判断是否所有字段正确，返回一个布尔值，传给testcase做判断
    #     if all_params == pass_params:
    #         assert True
    #     else:
    #         logging.error("通过字段：{}".format(pass_params))
    #         logging.error("共有{}个字段，有{}个字段出错".format(all_params ,(all_params-pass_params)))
    #         assert False