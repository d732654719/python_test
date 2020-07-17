
# 解释器
# def llop(name):
#     return name+" hi"
# print(llop("zj"))
#
# a=llop
# print(a("xx"))
# del llop
# print(llop("2"))
# print(a("23dds"))


# def hi(name="yasoob"):
#     def greet():
#         return "now you are in the greet() function"
#
#     def welcome():
#         return "now you are in the welcome() function"
#
#     if name == "yasoob":
#         return greet
#     else:
#         return welcome
#
#
# a = hi()
# print(a)
# # outputs: <function greet at 0x7f2143c01500>
#
# # 上面清晰地展示了`a`现在指向到hi()函数中的greet()函数
# # 现在试试这个
# print(a())

# """
# 被修饰函数需要传参是的写法，在定义 wrapper 函数的时候指定参数
# 需要传多个参数是或者传不定个数的参数时，可以用*args,
# 需要传关键字参数使，那么使用**kwargs
# """
# from functools import wraps
# def a_decorator(func):
#     @wraps(func)
#     def warp_the_functin(*args,**kwargs):
#
#         return func(*args,**kwargs) + "\n I am from china"
#     return warp_the_functin
#
# @a_decorator
# def a_function_need_decorated(name,address,phone="158888888"):
#     return "hi "+name+address+"\nmy number is:"+phone
# print(a_function_need_decorated("fj","a"))

# """
# 带参数的装饰器
# """
# import logging
# def logger(level):
#     def decorator(func):
#         def wrap(*args):
#             if level=="warn":
#                 logging.warning("{} is running".format(func.__name__))
#             elif level=="info":
#                 logging.info("{} is running".format(func.__name__))
#             return func(*args)
#         return wrap
#     return decorator
#
# @logger(level="info")
# def some(name):
#     print("{} is unstoppable".format(name))
#
# some("thones")

# class Foo(object):
#     def __init__(self, func):
#         self._func = func
#
#     def __call__(self):
#         print ('class decorator runing')
#         self._func()
#         print ('class decorator ending')
#
# @Foo
# def bar():
#     print ('bar')
#
# bar()
# "def __init__(self, driver: WebDriver) 怎么解释"
import logging
import time
import os




