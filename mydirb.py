import os
import re
import sys
import urlparse
def usage():
    print "usage:%s targets_file" % sys.argv[0]
    print "eg:"
    print "%s bing_http_domain_list.txt" % sys.argv[0]

def main():
    if len(sys.argv)!=2:
        usage()
    else:
        start()

def get_domain_name(uri):
    uri=urlparse.urlparse(uri)
    name=uri.hostname
    name=re.sub(r'(https://)|(http://)|(\s)|(/.*)|(:.*)',"",name)
    return name

def write_scan_log_to_mysql(http_domain,strings_to_write):
    import MySQLdb
    try:
        conn=MySQLdb.connect(host="192.168.3.13",user="root",passwd="root",db="seng",port=3306)
        cur=conn.cursor()
        #dec is a key word in mysql,so we should add `` here
        sql2 = "update web_pangzhan set `dec`='%s' where webinfo='%s'" % (strings_to_write,http_domain)
        #print sql2
        cur.execute(sql2)
        conn.commit()
        cur.close()
        conn.close()
    except Exception,ex:
        print ex

def start():
    os.system("mkdir dirb_log")
    f=open(sys.argv[1],"a+")
    all=f.readlines()
    f.close()
    for each in all:
        each=re.sub(r'(\s)',"",each)
        os.system("dirb %s -o dirb_log/%s_log.txt" % (each,get_domain_name(each)))
        output_file_name="dirb_log/%s_log.txt" % get_domain_name(each)
        #print "output_file_name is:%s" % output_file_name
        f=open(output_file_name,"r+")
        strings_to_write=f.read()
        f.close()
        write_scan_log_to_mysql(each,strings_to_write)

if __name__=='__main__':
    main()

