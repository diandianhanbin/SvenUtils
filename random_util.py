# ecoding=utf-8
# Author: Sven_Weng
# Web   : http://www.wengyb.com
"""
随机数相关操作的公共库


"""
import random
import uuid


def get_rand_int(num):
    """
    获取指定位数的随机数
    eg：
        get_rand_int(5) ==> 32789
        get_rand_int(4) ==> 3326
    :param num: int，指定位数
    :return: int
    """
    tmp = 10 ** (num - 1)
    return random.randint(tmp, 9 * tmp)


def get_uuid():
    """
    获取一个没有连接符的uuid
    :return:
    """
    uid = str(uuid.uuid4())
    return uid.replace('-', '')
