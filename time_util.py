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


def timestamp2datetime(value, time_format='%Y-%m-%d %H:%M:%S'):
    """
    将 整形 的时间戳 按照format转换成 字符串
    :param value: int, 整形时间戳
    :param time_format: str, 字符串格式
    :return: 返回字符串形式的时间字符串
    """
    value = time.localtime(value)
    dt = time.strftime(time_format, value)
    return dt