# ecoding=utf-8
# Author: Sven_Weng
# Web   : http://www.wengyb.com
"""
网络请求相关的公共方法
"""
import socket


def tcp_client(ip, port, data, buffer=2048):
    """
    执行TCP请求
    :param ip: str, ip
    :param port: int, 端口
    :param data: str, 请求的数据
    :param buffer: int, 缓冲区大小，默认2048
    :return:str, 返回的内容
    """
    addr = (ip, int(port))
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(addr)
    client.sendall(data)
    recv = client.recv(buffer)
    client.close()
    return recv


def unix_socket_send(srv_addr, req_text, timeout=5):
    """
    发送unix socket请求
    :param srv_addr: UnixSocket文件的地址
    :param timeout: 超时时间(s)
    """
    server_address = srv_addr
    clt_sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
    clt_sock.settimeout(timeout)
    try:
        clt_sock.sendto(req_text, server_address)
    finally:
        clt_sock.close()


def unix_socket_send_and_recv(srv_addr, req_text, timeout=5, buffer_size=2048):
    """
    发送unix socket请求并接受返回
    :param srv_addr: str, UnixSocket文件的地址
    :param req_text: str, 请求的内容
    :param timeout: int, 超时时间
    :param buffer_size: int, 缓冲区大小，默认2048
    :return: str, 返回的内容
    """
    server_address = srv_addr
    clt_sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
    clt_sock.settimeout(timeout)
    try:
        clt_sock.sendto(req_text, server_address)
        data, address = clt_sock.recvfrom(buffer_size)
    finally:
        clt_sock.close()
    return data


def get_localhost_ip():
    """
    通过发送一个udp请求来获取本机ip
    :return:str, 本机ip
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip
