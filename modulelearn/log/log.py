import logging
import time
import os
path= os.path.dirname(os.path.abspath(__file__))
log_path = os.path.join(path,"logfile")
class Mylogger:
    def __init__(self):

        # 创建logger容器
        self.logger = logging.getLogger('weblog')
        self.logger.setLevel("DEBUG")
        # 创建输出渠道
        now = time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime())
        fh = logging.FileHandler(log_path + '/{}_web.log'.format(now), encoding='utf-8')
        sh = logging.StreamHandler()
        fh.setLevel(logging.INFO)
        sh.setLevel(logging.INFO)
        # 格式设置
        formatter =logging.Formatter("%(name)s|%(levelname)s|%(asctime)s|%(filename)s|【日志信息】：%(message)s",
                                     "%Y-%m-%d %H:%M:%S")
        fh.setFormatter(formatter)
        sh.setFormatter(formatter)
        self.logger.addHandler(fh)
        self.logger.addHandler(sh)
        fh.close()
        sh.close()
    def debug(self,massage):
        return self.logger.debug(massage)

    def info(self, massage):
        return self.logger.info(massage)

    def warning(self, massage):
        return self.logger.warning(massage)

    def error(self, massage):
        return self.logger.error(massage)

    def critical(self, massage):
        return self.logger.critical(massage)
        #?


if __name__ == '__main__':
        log= Mylogger()
        log.debug("一个dubug信息")
        log.info("一个info信息")
        log.warning("一个wanrning信息")
        log.error("一个error信息")
        log.critical("一个critical信息")
