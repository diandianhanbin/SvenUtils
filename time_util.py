# ecoding=utf-8
# Author: Sven_Weng
# Web   : http://www.wengyb.com
"""
日期时间相关的公共方法
"""
import time


def get_time_str(fmt):
    """
    根据fmt的值返回字符串格式的时间。
    eg：
        get_time_str("%Y-%m-%d %H:%M:%S") ==> 2019-02-01 15:19:45
        get_time_str("%Y-%m-%d") ==> 2019-02-01
    :param fmt:str, 表达式
    :return:str
    """
    return time.strftime(fmt, time.localtime())
