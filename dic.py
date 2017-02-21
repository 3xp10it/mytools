#############################################################
###                                                  
###   mmmm                mmm     mmmm    "      m   
###  "   "# m   m  mmmm     #    m"  "m mmm    mm#mm 
###    mmm"  #m#   #" "#    #    #  m #   #      #   
###      "#  m#m   #   #    #    #    #   #      #   
###  "mmm#" m" "m  ##m#"  mm#mm   #mm#  mm#mm    "mm 
###                #                                 
###                "                                 
###                                                          
### name: dic.py
### function: clean dict
### date: 2016-10-07
### author: quanyechavshuo
### blog: https://3xp10it.github.io
#############################################################
import time
from exp10it import *
figlet2file("3xp10it","/tmp/figletpic",True)
time.sleep(1)

import sys
import re
def usage():
    print("example:%s -f file.txt" % sys.argv[0])
    print("there will be a newfile.txt in the same directory.")
    sys.exit(0)
def main():
    if sys.argv[1]!='-f':
        usage()
    file=open(sys.argv[2],"r+")
    list=file.readlines()
    file.close()
    
    
    for each in list:
        each=re.sub(r"(\s)$","",each)
        newfile=open("newfile.txt","a+")
        new_list=newfile.readlines()
        if each+'\r\n' not in new_list:
            newfile.write(each+'\r\n')
        newfile.flush()
        newfile.close()


if __name__=="__main__":
    main()
