# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#upon 4 lines for chinese support
import time
#from exp10it import *
#figlet2file("3xp10it",2,True)
time.sleep(1)

###
### name: 2
### function: dic handle the same lines
### date: 2016-08-04
### author: quanyechavshuo
### blog: https://3xp10it.github.io
#############################################################


#简单字典去重脚本
import sys
def usage():
	print "example:%s -f file.txt" % sys.argv[0]
	print "there will be a newfile.txt in the same directory."
	sys.exit(0)
def main():
	if sys.argv[1]!='-f':
		usage()
	file=open(sys.argv[2],"r+")
	list=file.readlines()
	file.close()


	for each in list:
		newfile=open("newfile.txt","a+")
		new_list=newfile.readlines()
		if each not in new_list:
			newfile.write(each)
		newfile.flush()
		newfile.close()


if __name__=="__main__":
	main()
