import os
import sys
def usage():
    print "usage:%s targets_file" % sys.argv[0]
    print "eg:"
    print "%s bing_http_domain_list.txt" % sys.argv[0]

def main():
    if len(sys.argv)!=2:
        usage()
    else:
        start()

def start():
    os.system("mkdir dirb_log")
    f=open(sys.argv[1],"a+")
    all=f.readlines()
    f.close()
    for each in all:
        os.system("dirb %s -o dirb_log/%s_log.txt" % (each,each))
        

if __name__=='__main__':
    main()

