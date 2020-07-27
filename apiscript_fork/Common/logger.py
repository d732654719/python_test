import logging, time
from Common.path_config import *
class Mylogger:
    now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
    # logger = logging.getLogger()
    sh = logging.StreamHandler()
    fh = logging.FileHandler(log_path + "/{}.log".format(now), encoding="utf-8")
    formatter = "[%(levelname)s]-[%(asctime)s]-日志信息:%(message)s"
    logging.basicConfig(level=logging.DEBUG,format=formatter, handlers=[fh, sh])
if __name__ =='__main__':
    logging.error("你的(配置项-用例编号)填写的数据类型不支持！只支持列表和元组")
    logging.info("替换后的请求地")


