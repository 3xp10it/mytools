import requests
import re
import random
import os
from exp10it import get_string_from_command

IPProxyPoolUrl = "http://192.168.8.240:8000/?types=0&count=100"


def get_random_proxy():
    IPPOOL = eval(requests.get(IPProxyPoolUrl).text)
    random_choose = random.choice(IPPOOL)
    proxy_addr = "http://" + \
        str(random_choose[0]) + ":" + str(random_choose[1])
    return proxy_addr


qihao_list = [
    '201502',
    '201503',
    '201504',
    '201505',
    '201506',
    '201507',
    '201508',
    '201509',
    '201510',
    '201511',
    '201512',
    '201601',
    '201602',
    '201603',
    '201604',
    '201605',
    '201606',
    '201607',
    '201608',
    '201609',
    '201610',
    '201611',
    '201612',
    '201701',
    '201702',
    '201703',
    '201704',
    '201705',
    '201706',
    '201707',
    '201708',
    '201709',
    '201710',
    '201711'
]

url = "http://xxx.xxx.xxx"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:51.0) Gecko/20100101 Firefox/51.0',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
           'Cookie': 'JSESSIONID=EA6DCEF9BA7D4ED7EA25B0377C20C092-n2.Tomcat1',
           'Connection': 'close',
           'Upgrade-Insecure-Requests': '1',
           'Content-Type': 'application/x-www-form-urlencoded',
           'Content-Length': '38'
           }
import threading
mutex = threading.Lock()
for qihao in qihao_list:
    i = 0
    post_js_content = '''
"use strict";
var page = require('webpage').create(),
    server = 'http://xxx.xxx.xxx',
    data = 'page_no=1&issue_number=%s&apply_code=';

page.settings.resource_timeout = 9999999999999;
page.settings.user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.%s Safari/537.36";

page.open(server, 'post', data, function (status) {
    if (status !== 'success') {
        console.log('Unable to post!');
    } else {
        console.log(page.content);
    }
    phantom.exit();
});
    ''' % (qihao, ++i)
    while True:
        os.system("rm post.js")
        with open("post.js", "a+") as f:
            f.write(post_js_content)
        proxy_addr = get_random_proxy()
        print(proxy_addr)
        html = get_string_from_command(
            "phantomjs post.js --proxy=%s" % proxy_addr)
        has_page_no = re.search(r"/(\d+)页", html)
        if has_page_no:
            break
        else:
            print("没有获取到页数,尝试再次获取...")
            continue

    page_no = has_page_no.group(1)
    print("期号:%s,页数:%s" % (qihao, page_no))
    page_list = []
    for page in range(1, int(page_no) + 1):
        page_list.append(str(page))

    def get_page_content(page):
        data = "page_no=%s&issue_number=%s&apply_code=" % (page, qihao)
        print("正在请求第%s期,第%s页..." % (qihao, page))
        rsp = requests.get(url, timeout=60)
        cookie = rsp.headers['Set-Cookie']
        # print(cookie)
        headers['Cookie'] = cookie
        proxy_addr = get_random_proxy()
        proxies = {}
        proxies_1 = proxy_addr.split(":")[0]
        proxies[proxies_1] = proxy_addr
        # print(proxies)
        html = requests.post(url, data.encode("utf-8"),
                             headers=headers, proxies=proxies, timeout=60).text
        a = re.findall(
            r'''class="content_data"[\s\S]*?<td\s*>(\d+)</td>[\s\S]*?<td\s*>(.+)</td>''', html)
        mutex.acquire()
        for each in a:
            with open("x.txt", "a+") as f:
                string_to_write = qihao + "    " + \
                    each[0] + "    " + each[1] + "\n"
                print(string_to_write)
                f.write(string_to_write)
        mutex.release()

    from concurrent import futures
    with futures.ThreadPoolExecutor(max_workers=20) as executor:
        executor.map(get_page_content, page_list)
