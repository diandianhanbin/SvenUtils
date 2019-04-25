# ecoding=utf-8
# Author: Sven_Weng
# Web   : http://www.wengyb.com
"""
字符串操作的公共方法
"""
import re


def str2map(reqstr):
    """
    把类似a=1&b=2的字符串转成字典类型
    :param reqstr:str，类似a=1&b=2的字符串
    :return:
    """
    reqarr = reqstr.split("&")
    reqmap = {}
    for astr in reqarr:
        tmpkv = astr.split("=")
        reqmap[tmpkv[0]] = ("" if len(tmpkv) == 1 else (
            tmpkv[1] if len(tmpkv) == 2 else (tmpkv[1] + "=" if len(tmpkv) == 3 else tmpkv[1] + "==")))
    return reqmap


def map2str(reqmap):
    """
    把字典转换为字符串
    :param reqmap: 字典
    :return:
    """
    tmp_str = ""
    for kv in sorted(reqmap.keys()):
        if len(kv) > 0:
            tmp_str = tmp_str + kv + "=" + str(reqmap[kv]) + "&"
    tmp_str = tmp_str[0:-1]
    return str(tmp_str)


def hump2underline(hunp_str):
    """
    驼峰形式字符串转成下划线形式
    :param hunp_str: 驼峰形式字符串
    :return: 字母全小写的下划线形式字符串
    """
    # 匹配正则，匹配小写字母和大写字母的分界位置
    p = re.compile(r'([a-z]|\d)([A-Z])')
    # 这里第二个参数使用了正则分组的后向引用
    sub = re.sub(p, r'\1_\2', hunp_str).lower()
    return sub


def underline2hump(underline_str):
    """
    下划线形式字符串转成驼峰形式
    :param underline_str: 下划线形式字符串
    :return: 驼峰形式字符串
    """
    # 这里re.sub()函数第二个替换参数用到了一个匿名回调函数，回调函数的参数x为一个匹配对象，返回值为一个处理后的字符串
    sub = re.sub(r'(_\w)', lambda x: x.group(1)[1].upper(), underline_str)
    return sub