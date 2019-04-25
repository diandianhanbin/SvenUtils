# ecoding=utf-8
# Author: Sven_Weng
# Web   : http://www.wengyb.com
"""
加解密相关的公共方法
"""
import base64
import hashlib


def de_base64(en_text):
    """
    base64解密方法
    :param en_text: str， base64加密串
    :return:
    """
    return base64.b64decode(en_text)


def en_base64(base64_text):
    """
    base64加密方法
    :param base64_text: str，需要加密的字符串原串
    :return:
    """
    return base64.b64encode(base64_text)


def get_md5_value(src):
    """
    :summary 计算MD5值
    :param src:  MD5值原串
    :return: MD5值
    """
    my_md5 = hashlib.md5()
    my_md5.update(src)
    my_md5_digest = my_md5.hexdigest()
    return my_md5_digest


def get_sha256(src):
    """
    :summary 计算SHA256值
    :param src:  SHA256值原串
    :return: SHA256值
    """
    sha256 = hashlib.sha256()
    sha256.update(src)
    return sha256.hexdigest()
