import os

#获取当前脚本路径+文件名的两种方法
current_address_1 = os.path.abspath(__file__)
current_address_2 = os.path.realpath(__file__)

#获取当前脚本路径的四种方法
current_file1 = os.path.split(current_address_1)[0]
current_file2 = os.path.dirname(current_address_2)
current_file3 = os.path.abspath(".")
current_file4 = os.getcwd()
# print(current_address_1, "\n", current_address_2, "\n",current_file1, "\n", current_file2)
# print(current_file3)
# print(current_file4)