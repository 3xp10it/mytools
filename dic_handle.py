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
