import os
import pdb
import html
import re
os.system("vim /tmp/xcss.txt")
with open("/tmp/xcss.txt","r+") as f:
    lines=f.readlines()
newlines=''
for line in lines:
    line=re.sub(r"<[^>]+>","",line)
    print(line)
    line=html.unescape(line)
    line=html.unescape(line)
    newlines+=line
os.system("rm /tmp/xcss1.txt")
with open("/tmp/xcss1.txt","a+") as f:
    f.write(newlines)
os.system("cat /tmp/xcss1.txt")
