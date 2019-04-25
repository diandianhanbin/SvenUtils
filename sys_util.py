# ecoding=utf-8
# Author: Sven_Weng
# Web   : http://www.wengyb.com
import ctypes


def get_tid():
    """
    获取线程的tid，这里调用的是c库的方法。
    :return: int, 线程的tid
    """
    sys_gettid = 186
    libc = ctypes.cdll.LoadLibrary('libc.so.6')
    tid = libc.syscall(sys_gettid)
    return tid
