#https://www.vultr.com/faq/
import re
from concurrent import futures
from exp10it import test_speed
from exp10it import get_request
a=get_request("https://www.vultr.com/faq/")
html=a['content']
a=re.search(r"Download Test File:([\s\S]+)Port X seems to be blocked on my VPS",html,re.I).group(1)
a=re.findall(r'''\s*(((?!\>).)+)\n.+\n.+\n\s*<a href="((?!\.bin).)+">(.+)</a>''',a,re.I)
quickest_time=999999
quickest_address=""
quickest_name=""

def get_speed(each):
    global quickest_time,quickest_address,quickest_name
    each_speed_time=test_speed(each[-1])
    if each_speed_time<quickest_time:
        quickest_time=each_speed_time
        quickest_address=each[-1]
        quickest_name=each[0]

with futures.ThreadPoolExecutor(max_workers=15) as executor:
    executor.map(get_speed,a)
print("quickest is:\n"+quickest_name+","+quickest_address+","+str(quickest_time)+"ms")

