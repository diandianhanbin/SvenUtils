# ecoding=utf-8
# Author: Sven_Weng
# Web   : http://www.wengyb.com
"""
通用日志模块

LOGFILENAME为打印日志的文件，最终的日志文件是 LOGFILENAME+日期
LOGPATH为日志的路径，路径最后一个 /  必须存在

使用方式：
    import logger_util as Logger
    Logger.info("test")
    Logger.debug("test")
"""
import logging
import os
import time
from threading import Lock

# 全局变量
LOGFILENAME = "sys"
LOGPATH = "./log/"

NeedAddStreamHandler = 0
NeedAddFileHandler = 0
logNowTime = '19700101'
lock = Lock()


# 下面还定义了全局变量 log=Logger()


class Logger:
    logger = None
    LogFileName = LOGFILENAME
    LogFileDir = LOGPATH  # the last '/' must exist
    Flevel = logging.DEBUG  # 将log打印到文件时的日志级别
    Slevel = logging.DEBUG
    formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
    fileHandler = None

    def __new__(cls):
        if '_inst' not in vars(cls):
            cls._inst = super(Logger, cls).__new__(cls)
            # print 'new'
        return cls._inst

    def __init__(self):
        self.logger = logging.getLogger(self.LogFileName)
        self.logger.setLevel(logging.DEBUG)

    def __str__(self):
        return "This Class ID is %s" % id(self)

    def add_stream_handler(self):
        global NeedAddStreamHandler
        if NeedAddStreamHandler == 1:
            # print "Has add FileHandler !"
            return
        # 设置CMD日志
        sh = logging.StreamHandler()
        sh.setFormatter(self.formatter)
        sh.setLevel(self.Slevel)
        self.logger.addHandler(sh)
        NeedAddStreamHandler = 1

    def add_file_handler(self):
        global NeedAddFileHandler, logNowTime
        if NeedAddFileHandler == 1:
            return
        # 设置File日志
        if not os.path.exists(self.LogFileDir):
            os.mkdir(self.LogFileDir)
        logNowTime = time.strftime('%Y%m%d', time.localtime(time.time()))
        self.fileHandler = logging.FileHandler(self.LogFileDir + self.LogFileName + "_" + logNowTime + "_app.log")
        self.fileHandler.setFormatter(self.formatter)
        self.fileHandler.setLevel(self.Flevel)
        self.logger.addHandler(self.fileHandler)
        NeedAddFileHandler = 1

    def check_file_handler(self):
        global NeedAddFileHandler, logNowTime, lock
        temp_time = time.strftime('%Y%m%d', time.localtime(time.time()))
        # 初始状态 logNowTime 是设置的默认值，肯定满足不了 tmpTime == logNowTime
        if temp_time == logNowTime and NeedAddFileHandler == 1:  # 大部分时间是处于这种状态
            return
        # 锁开始
        lock.acquire()
        try:
            if NeedAddFileHandler == 1 and temp_time != logNowTime:
                # isAddFileHandler等于1，表示已经调用过addFileHandler()
                # 时间不等，表示日期切换，需要切换日志文件，先remove在add
                self.logger.removeHandler(self.fileHandler)
                NeedAddFileHandler = 0  # 只有初始值和这里，才会设置 NeedAddFileHandler=0
            # 若前面所有if都没进去，表示程序第一次启动 NeedAddFileHandler = 0
            self.add_file_handler()
            lock.release()
        except Exception:
            lock.release()
        # 锁结束

    def debug(self, message):
        self.check_file_handler()
        self.logger.debug(message)

    def info(self, message):
        self.check_file_handler()
        self.logger.info(message)

    def warn(self, message):
        self.check_file_handler()
        self.logger.warn(message)

    def error(self, message):
        self.check_file_handler()
        self.logger.error(message)

    def crit(self, message):
        self.check_file_handler()
        self.logger.critical(message)


# 全局变量
log = Logger()


# 下面的函数，期望通过模块直接调用，不再初始化一个Logger()实例
def debug(message):
    global log
    log.check_file_handler()
    log.debug(message)


def info(message):
    global log
    log.check_file_handler()
    log.info(message)


def warn(message):
    global log
    log.check_file_handler()
    log.warn(message)


def error(message):
    global log
    log.check_file_handler()
    log.error(message)


def crit(message):
    global log
    log.check_file_handler()
    log.crit(message)


# Logger类测试
def class_test():
    logyyx = Logger()
    logyyx.add_file_handler()

    logyyx.info('一个debug信息')
    logyyx.info('一个info信息')
    logyyx.warn('一个warning信息')
    logyyx.error('一个error信息')
    logyyx.crit('一个致命critical信息')
    logxx = Logger()
    logxx.add_file_handler()
    logxx.info('ddddddd')
    a = Logger()
    print 'NeedAddFileHandler  %s' % NeedAddFileHandler
    a.isAddStreamHandler = 1
    b = Logger()
    b.add_stream_handler()
    print 'NeedAddStreamHandler   %s' % NeedAddStreamHandler
    print 'NeedAddFileHandler  %s' % NeedAddFileHandler


# 模块函数测试
def module_test():
    debug("====== debug ======")
    info("====== info ======")
    warn("====== warn ======")
    error("====== error ======")
    crit("====== crit ======")


if __name__ == '__main__':
    module_test()
