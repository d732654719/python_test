from modulelearn.log.log import Mylogger
log=Mylogger.info("log1")

def foo():
    log.info("进行阶乘")
    try:
        a=input("a=")
        a=int(a)
    except Exception as e:
        log.info("输入了非数字数据")
        log.info(e)
    res = 1
    for i in range(1,a+1):
        res*=i

foo()
