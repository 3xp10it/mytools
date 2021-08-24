import sys
import os
import pdb
import re
kindle_file="/Volumes/Kindle/documents/My Clippings.txt"
if not os.path.exists(kindle_file):
    print("未找到kindle笔记文件,请检查")
    sys.exit(0)
with open(kindle_file,"r") as f:
    txt=f.read()
title=input("请输入书名:\n")
_list=re.findall(r"=+\n%s.*\n.+?\n\n([^=\n]+)" % title,txt)
with open("/tmp/1","w") as f:
    for line in _list:
        f.write(line+"\n")
print("已经将kindle中%s的笔记导入到/tmp/1")
