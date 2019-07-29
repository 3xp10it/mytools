# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#必须加上上面四行,否则各种编码的错误爆出
import urllib2

def getip():
    return "113.116.175.200"
url="http://ip.taobao.com/service/get_ip_info.php?ip=%s" % (getip())
response = urllib2.urlopen(url)
html = response.read()
import json
json_html=json.loads(html)
print json_html['data']['country']
print json_html['data']['city']
print json_html['data']['region']

