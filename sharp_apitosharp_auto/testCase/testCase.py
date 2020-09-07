import unittest
# 再创建一个存储sa和deli数据的断言标准的列表的存储模块
from common.data_handle import gener_complete_sa_list, gener_complete_deli_list
import logging
from common.assert_stand import *
logging.basicConfig(level=logging.INFO)
class ftp_test(unittest.TestCase):

    def test_deli_sample(self):
        l = gener_complete_deli_list()
        # n代表只能是数字
        assert_a = assert_deli
        # 处理原生的切割数据，使字符串尾部的空格去掉
        a = []
        for i in l:
            if i.isspace():
                a.append(i)
            else:
                a.append(i.rstrip())
        all_params = len(a)
        pass_params = 0
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
            # 缺少处理000.000类似的数据的步骤，和+001的数据应该一起处理后，判断是否是数字，处理日语数据
            # 判断字符的类型是否正确,标志位：n:除日期外数字,d:日期,p:带小数点数字,+:数字加中间的+,+n:+加数字,m:其他
            sign = ""
            if a[i].isdigit():
                if is_valid_date(a[i]):
                    sign = "d"
                else:
                    sign = "n"

            # 判断段小数点数字是否正确
            elif "." in a[i]:
                sign = count_after_point(a[i])

            # 添加+号判断
            elif "+" in a[i]:
                s = a[i].split("+")
                count = len(s)
                if count != 2 or len(s[1])!= 3:
                    sign = 'm'
                else:
                    real_count = 0
                    for x in s:
                        if x.isdigit():
                            real_count += 1
                    if real_count == 2:
                        sign = '+'
                    elif real_count == 1 and s[0]=='':
                        sign ='+n'
                    else:
                        sign = 'm'

            else :
                sign = "m"
            if sign in assert_a[i][0]:
                pass_params += 1
            else:
                logging.error("错误,sign={},assert_a[{}]={},出错行头是：'{}'，第{}个字段出错，字段类型错误，内容：'{}'".format(sign,i,assert_a[i][0],a[0], i + 1, a[i]))

        # 判断是否所有字段正确，返回一个布尔值，传给testcase做判断
        if all_params == pass_params:
            assert True
            logging.info("所有字段验证通过")
        else:
            logging.error("通过字段：{}".format(pass_params))
            logging.error("共有{}个字段，有{}个字段出错".format(all_params, (all_params - pass_params)))
            assert False

    def test_sa_sample(self):
        # 获取按字段分割后的存在列表中的sa数据
        a = gener_complete_sa_list()
        # T代表必填
        assert_a = assert_sa
        # 处理原生的切割数据，使字符串尾部的空格去掉
        for i in range(0, len(a)):
            for j in range(0, len(a[i])):
                if a[i][j].isspace():
                    continue
                else:
                    a[i][j] = a[i][j].rstrip()
        all_params = 0
        for i in a:
            
            all_params += len(i)
        pass_params = 0
        # 遍历所有字段
        for i in range(0, len(a)):
            # 结合分割数据的0,1位，当做匹配断言标准的条件
            data_head=a[i][0]+a[i][1]

            for j in range(0, len(a[i])):
                # 是否允许为空为第一个判断
                if a[i][j].isspace():
                    if assert_a[data_head][j][1] == "T":
                        logging.error("错误,文件的第{}行,出错行头是:'{}',该行第{}个字段出错,不能为空,内容:'{}'".format(i+1,a[i][0], j + 1, a[i][j]))
                    else:
                        pass_params += 1
                    continue
                # 判断字符打头是否是空
                if a[i][j][0] == " " and a[i][j][-1] != " ":
                    logging.error("错误,文件的第{}行,出错行头是:'{}',第{}个字段出错,字段开头不能为空,可能该行有错位,内容:'{}'".format(i+1,a[i][0], j + 1, a[i][j]))
                    continue
                # 判断固定值是否正确
                if len(assert_a[data_head][j]) == 3:
                    if assert_a[data_head][j][2] == a[i][j]:
                        pass_params += 1
                    else:
                        logging.error("错误,文件的第{}行,出错行头是:'{}',该行第{}个字段出错,固定值值出错,内容:'{}'".format(i+1,a[i][0], j + 1, a[i][j]))
                    continue

                # 判断字符的类型是否正确
                sign = ""
                if a[i][j].isdigit():
                    sign=int_data_sort(a[i][j])
                else:
                    sign = "m"
                if sign in assert_a[data_head][j][0] or assert_a[data_head][j][0] in sign:
                    pass_params += 1
                else:
                    logging.error("错误,文件的第{}行，出错行头是：'{}'，第{}个字段出错，字段实际类型={},字段预期类型={},字段内容：'{}'".format(i+1, a[i][0]+a[i][1], j + 1, sign, assert_a[data_head][j][0],a[i][j]))

        # 判断是否所有字段正确，返回一个布尔值，传给testcase做判断
        if all_params == pass_params:
            logging.info("所有字段验证通过")
            assert True
        else:
            logging.error("通过字段：{}".format(pass_params))
            logging.error("共有{}个字段，有{}个字段出错".format(all_params, (all_params - pass_params)))
            assert False

