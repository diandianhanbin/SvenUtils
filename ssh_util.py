# ecoding=utf-8
# Author: Sven_Weng
# Web   : http://www.wengyb.com
"""
通过SSH执行远程命令，依赖paramiko库

实例化SSHClient时必须传入SSHClientObj对象

eg：
    ssh_obj = SSHClientObj()
    ssh_obj.ip = "127.0.0.1"
    ssh_obj.port = 1234
    ssh_obj.username = "svenweng"
    ssh_obj.password = "123456"
    ssh_client = SSHClient(ssh_obj)
    ssh_client.ssh_exec_and_recv("ls")
"""
import paramiko


class SSHClientObj(object):
    """
    SSH连接的参数对象
    """

    def __init__(self):
        self.ip = ""
        self.port = ""
        self.username = ""
        self.password = ""


class SSHClient(object):
    def __init__(self, SSHClientObj):
        self.ip = SSHClientObj.ip
        self.port = SSHClientObj.port
        self.username = SSHClientObj.username
        self.password = SSHClientObj.password

    def ssh_exec_and_recv(self, cmd):
        """
        执行远程命令，并返回结果
        :param cmd: str，命令串
        :return: str，执行后的结果
        """
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=self.ip, port=self.port, username=self.username, password=self.password)
        stdin, stdout, stderr = ssh.exec_command(cmd)
        result = stdout.read()
        return result

    def ssh_exec(self, cmd):
        """
        仅执行远程命令
        :param cmd: str，命令串
        :return:
        """
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=self.ip, port=self.port, username=self.username, password=self.password)
        ssh.exec_command(cmd)
