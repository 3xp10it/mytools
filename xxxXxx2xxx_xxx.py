# usage:python3 xxxXxx2xxx_xxx.py file.py
# 批量替换:for file in $(find . -name "*.py");do python3 xxxXxx2xxx_xxx.py
# $file;done
import sys
import re
import os
with open(sys.argv[1], "r+") as f:
    string = f.read()
# xxxX...->xxx_xxxx
# eg.nihHao->nih_hao
# eg.niHaMa->ni_hama
if re.search(r"\W(([a-z_]+)([A-Z])(\w+))\W", string):
    os.system("cp -p %s /tmp/" % sys.argv[1])
    print("bak file:/tmp/%s" % sys.argv[1])
else:
    print("%s needn't modify" % sys.argv[1])
    sys.exit(0)

while re.search(r"\W(([a-z_]+)([A-Z])(\w+))\W", string):
    xxxXxxx = re.findall(r"\W(([a-z_]+)([A-Z])(\w+))\W", string)
    for each in xxxXxxx:
        _x = "_" + chr(ord(each[2]) + 32)
        xxx_xxx = each[1] + _x + each[3]
        string = string.replace(each[0], xxx_xxx)
os.system("rm %s" % sys.argv[1])
with open(sys.argv[1], "a+") as f:
    f.write(string)
print("%s content updated" % sys.argv[1])
