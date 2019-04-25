# ecoding=utf-8
# Author: Sven_Weng
# Web   : http://www.wengyb.com


def express_get_json_value(express, json_ori):
    """
    用表达式的方式获取一个json的值
    :param express: 表达式，类似a.b.c
    :param json_ori:json的原串
    :return: str，获取的值，如果没有值则返回空
    """
    if "." not in express:
        return json_ori[express]
    tmp_list = express.split(".")
    tmp = json_ori
    for x in tmp_list:
        tmp = tmp.get(x, '')
    return tmp
