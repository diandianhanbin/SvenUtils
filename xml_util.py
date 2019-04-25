# ecoding=utf-8
# Author: Sven_Weng
# Web   : http://www.wengyb.com
"""
XML操作的公共方法
"""
import re
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


def xml2dict(src):
    """
    转换整个xml字符串为字典类型，此方法比较适用于k-v类型的xml文件，行内value多的xml文件不适合使用此方法
    :param src: str， xml文件的字符串
    :return: dict
    """
    tree = ET.XML(src)
    xmldict = _XmlDictConfig(tree)
    return xmldict


def innerxml2dict(src):
    """
    转换xml行内值为字典
    eg：
        <limit name="wx_public_api_offline" index="4" global_max_quota="80000" set_max_quota="10000" cgi_type="fast_cgi" semkey="50004" applyquota="20" highest="1.5"></limit>
        >>>>>
        {'index': '4', 'set_max_quota': '10000', 'name': 'wx_public_api_offline', 'global_max_quota': '80000', 'cgi_type': 'fast_cgi', 'semkey': '50004', 'applyquota': '20'}
    :param src:str， xml航黑的原串
    :return: dict
    """
    pattner = re.compile(r'([A-Za-z_]+="[A-Za-z0-9_\.]+")')
    v_pattner = re.compile(r'"([A-Za-z0-9_\.]+)"')
    dict_data = {}
    for x in re.findall(pattner, src):
        dict_data[x.split("=")[0]] = re.search(v_pattner, x.split("=")[1]).group(1)
    return dict_data


class _XmlListConfig(list):
    def __init__(self, aList):
        for element in aList:
            if element:
                # treat like dict
                if len(element) == 1 or element[0].tag != element[1].tag:
                    self.append(_XmlDictConfig(element))
                # treat like list
                elif element[0].tag == element[1].tag:
                    self.append(_XmlListConfig(element))
            elif element.text:
                text = element.text.strip()
                if text:
                    self.append(text)


class _XmlDictConfig(dict):
    def __init__(self, parent_element):
        if parent_element.items():
            self.update(dict(parent_element.items()))
        for element in parent_element:
            if element:
                if len(element) == 1 or element[0].tag != element[1].tag:
                    aDict = _XmlDictConfig(element)
                else:
                    aDict = {element[0].tag: _XmlListConfig(element)}
                if element.items():
                    aDict.update(dict(element.items()))
                self.update({element.tag: aDict})
            elif element.items():
                self.update({element.tag: dict(element.items())})
            else:
                self.update({element.tag: element.text})
