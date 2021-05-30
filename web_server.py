import pdb
from urllib.parse import quote,unquote
from urllib.parse import parse_qs
import threading
import os
import subprocess
import re
import platform
SYSTEM=platform.system()
current_abs_path=os.path.split(os.path.realpath(__file__))[0]


def file_server():
    html_abs_path=os.path.split(os.path.realpath(__file__))[0]+"/html"
    os.chdir(html_abs_path)
    if SYSTEM=='Windows':
        cmd="python -m http.server 80"
    else:
        cmd="python3 -m http.server 80"
    subprocess.Popen(cmd,shell=True)
    os.chdir(current_abs_path)


def start_web_server(host,port,rules):
    #eg.rules={'GET':get,'POST':post}
    #def get(self):
    #    from urllib.parse import parse_qs
    #    headers = str(self.headers)
    #    if self.path!='/favicon.ico':
    #        query_dict=parse_qs(self.path[2:])
    #        #注意,下面这行_set_headers()是必须加上的,否则浏览器访问当前服务会异常
    #        self._set_headers()
    #        self.wfile.write(bytes(str(query_dict), "utf-8"))
    #start_web_server(host='0.0.0.0',port=8888,rules=rules)
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from socketserver import ThreadingMixIn
    from urllib.parse import parse_qs

    class ThreadingHttpServer(ThreadingMixIn, HTTPServer):
        pass

    class S(BaseHTTPRequestHandler):
        def _set_headers(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

        def do_GET(self):
            rules['GET'](self)

        def do_POST(self):
            rules['POST'](self)

        def log_message(self, format, *args):
            if 'get_zs_zf' in self.path or 'get_rqpm_zf' in self.path:
                #这两种日志不打印(因为每秒都有一条)
                return

    def run(server_class=ThreadingHttpServer, handler_class=S):
        server_address = (host, int(port))
        httpd = server_class(server_address, handler_class)
        print('Starting api server on:'+str(port))
        httpd.serve_forever()

    run()

def web_server():
    def post(self):
        headers = str(self.headers)
        if self.path[:5]=='/test':
            datas = self.rfile.read(int(self.headers['content-length']))
            query_dict=parse_qs(datas.decode("utf8"),keep_blank_values=True)
            return_string={"result":"ok"}
        self.wfile.write(bytes(return_string, "utf-8"))

    def get(self):
        headers = str(self.headers)
        if self.path!='/favicon.ico':
            if self.path[:6]=='/test?':
                query_dict=parse_qs(self.path[8:],keep_blank_values=True)
                callback=query_dict['callback'][0]
                return_dict={"result":"ok"}
                return_string=callback+"("+str(return_dict)+")"

            self._set_headers()
            self.wfile.write(bytes(return_string, "utf-8"))

    rules={'GET':get,'POST':post}
    start_web_server(host='0.0.0.0',port=8888,rules=rules)


t=threading.Thread(target=file_server)
t.start()
web_server()
