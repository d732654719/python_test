# try:
#     a=1
#     b=0
#     c=a/b
#     print(c)
# except Exception as e:
#     print('error:{}'.format(e))
#     # raise e
#
# else:
#     print('else')
# import  re,sheet
# a='{"statuscode":"200"}'
#
# b=re.split(r"[;,\n]",a)
# print(b)

import re

# a="s2"
# c=re.match('\d',a)
# b=re.match('\w',a)
# d=re.match("^(\d+)(.*)",a)
# print(c)
# print(b)
# print(d)

# a = 'xxIxxjshdxxlovexxsffaxxpythonxx'
# list2='123'
# list3='des'
# infos = re.search('xx(.*)xx', a)
# c = re.match('[0-9]',list2)
# b = re.match("^(\d+)(.*)", a)
# print(infos)
# print(c)

import random,string
# def  data_is(datatype):
#   data_is={"字母":string.ascii_letters,"数字":string.digits,"特殊符号":string.punctuation,
#            "中文":chr(random.randint(0x4E00,0x9FA5))}
#   return
# n=8
# def data():
#     datas = ''.join(random.sample(data_is(datatype), n))
#     print(datas)
# a='abcdedf'
# b=a[2:4]
# print(b)
# datas = ''.join(random.sample(string.ascii_lowercase+string.digits, 5))
# print(datas)

# num1=string.ascii_letters+string.digits+string.punctuation
# str=''.join(random.sample(num1,10))
# print(str)
# passwd=''
# for i in range(10):
#     num = chr(random.randint(0x4E00, 0x9FA5))
#     passwd+=num
#
# print(passwd)
# for i in range(1,10):
#     print(i)
# a,b,c=1,2,3
# print(a,b,c)
# StopIteration()

# class Fab(object):
#
#     def __init__(self, max):
#         self.max = max
#         self.n, self.a, self.b = 0, 0, 1
#
#     def __iter__(self):
#         return self
#
#     def next(self):
#         if self.n < self.max:
#             r = self.b
#             self.a, self.b = self.b, self.a + self.b
#             self.n = self.n + 1
#             return r
#         # raise StopIteration()
#
# for n in Fab(5):
#     print (n)


# def fab(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b  # 使用 yield
#         # print b
#         a, b = b, a + b
#         n = n + 1
#
# for i in fab(6):
#     print(i)
import time


# log_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
# a = "logtime"+log_time
# print(type(a))
#
# b=os.path.abspath(".")
# print(b)

flist = []
for i in range(4):
    def foo(x):
        print(x+i)
    flist.append(foo)
for f in flist:
    f(2)


