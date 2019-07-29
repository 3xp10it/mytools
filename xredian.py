import pdb
import os
import re
import time
from exp10it import get_home_path
tmp_file=get_home_path()+"/Downloads/"+str(time.time())+".txt"
os.system("/Applications/MacVim.app/Contents/MacOS/Vim %s" % tmp_file)
with open(tmp_file,"r+") as f:
    content=f.read()
stock_list=re.findall(r"(\d{6})",content)
str_to_write=""
for stock in stock_list:
    str_to_write+=(stock+"\n")
with open(tmp_file,"w+") as f:
    f.write(str_to_write)
