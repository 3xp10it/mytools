import re
import os
os.system("pip3 install exp10it -U --no-cache")
from exp10it import post_request
while 1:
    postUrl = "http://javatools.bejson.com/tools/convert/hexChar"
    ox = input("Please input your string from hopper:>")
    if re.match(r"\\[^\\]+", ox):
        # 只有一个\符号
        pass
    if re.match(r"\\{2}", ox):
        # 有两个\符号
        ox = re.sub(r"\\{2}", r"\\", ox)
    data = {}
    data['oldStr'] = ox
    data['fmtType'] = 'c'
    req = post_request(postUrl, data)
    result = re.search(r'''message('|"):('|")(.*?)('|")''', req, re.I).group(3)
    print(result)
