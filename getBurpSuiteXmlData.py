import re
import base64
with open("out.txt","r+") as f:
    all=f.read()
g=re.findall(r"<request base64=.*>.*</request>",all)
out_list=[]
for each in g:
    tmp=re.search(r".*\[.*\[(.*)\]\]",each).group(1)
    btmp=tmp.encode(encoding="utf-8")
    tmp=base64.b64decode(btmp)
    tmp=tmp.decode()
    tmp=re.search(r"PASSWORD=(.*?)&",tmp).group(1)
    out_list.append(tmp)
#print(out_list)
for each in out_list:
    with open("riskuser.txt","a+") as f:
        f.write(each+"\r\n")
