import logging, re
from openpyxl import load_workbook
from Common.path_config import *
class do_excel:
    def read_sheet(self,sheetname):
        wb = load_workbook(exc_path)
        sh = wb[sheetname]
        title_data = []
        for i in range(1, sh.max_column+1):
            title_data.append(sh.cell(row=1, column=i).value)
        test_data=[]
        for i in range(2, sh.max_row+1):
            dict = {}
            for j in range(1, sh.max_column+1):
                if sh.cell(row=i, column=j).value =="无":
                    dict[title_data[j+1]] = " "
                else:
                    if j == sh.max_column and sheetname == "测试用例":
                        dict[title_data[j+1]] = re.split("[,;\n]", sh.cell(row=i, column=j).value)
                    else:
                        dict[title_data[j+1]] = sh.cell(row=i, column=j).value
            test_data.append(dict)
        return test_data
    def read_config(self,sheetname):
        test_data = self.read_sheet("测试用例")
        test_cof = self.read_sheet("配置")[0]
        for case in test_data:
            case["接口地址"]=test_cof["服务器地址"]+case["接口地址"]

if __name__ == '__main__':
    data = do_excel().read_sheet("测试用例")
    print(data)

