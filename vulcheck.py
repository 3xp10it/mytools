#使用说明
#python3 xxx.py package.txt targets.txt 'secret'
#python3 xxx.py 包文件 目标列表文件 返回内容中存在漏洞的正则表达式
import re
from concurrent import futures
from exp10it import send_http_packet
from urllib.parse import urlparse
import sys
package_file=sys.argv[1]
targets_file=sys.argv[2]
pattern_string=sys.argv[3]
pattern=re.compile(pattern_string,re.I)

with open(package_file,"r+") as f:
    package=f.read()
with open(targets_file,"r+") as f:
    targets=f.readlines()

def send_single_package(each):
    global package
    each=re.sub(r"\s$","",each)
    parsed=urlparse(each)
    host=parsed.netloc
    each_package=re.sub(r"(?<=Host: )(.+)",host,package,re.I)
    each_package=re.sub(r"(?<=Referer: )(.+)",each,each_package,re.I)
    a=send_http_packet(each_package,each.split(":")[0])['html']
    if pattern.search(a):
        print("%s 漏洞存在" % each)

with futures.ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(send_single_package,targets)

