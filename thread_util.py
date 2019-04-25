# ecoding=utf-8
# Author: Sven_Weng
# Web   : http://www.wengyb.com
"""
线程相关的公共方法
"""
from threading import Timer


def start_scheduler(recycle_time, func):
    """
    开启一个定时器
    :param recycle_time: int，多少秒执行一次
    :param func: 执行的函数，不带参数
    :return: obj， 定时器的对象，用于定时器停止
    """
    scheduler = _Scheduler(recycle_time, func)
    scheduler.start()
    return scheduler


def stop_scheduler(scheduler_obj):
    """
    定时器的停止方法
    :param scheduler_obj: obj， 定时器启动时返回的对象
    :return: None
    """
    scheduler_obj.stop()


class _Scheduler(object):
    def __init__(self, sleep_time, func):
        self.sleep_time = sleep_time
        self.function = func
        self._t = None

    def start(self):
        if self._t is None:
            self._t = Timer(self.sleep_time, self._run)
            self._t.start()
        else:
            raise Exception("this timer is already running")

    def _run(self):
        self.function()
        self._t = Timer(self.sleep_time, self._run)
        self._t.start()

    def stop(self):
        if self._t is not None:
            self._t.cancel()
            self._t = None
