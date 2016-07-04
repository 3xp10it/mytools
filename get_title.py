
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#必须加上上面四行,否则各种编码的错误爆出
import re
import urllib2
import urllib
import time
from urlparse import *
def get_uris_from_file(file):
    f=open(file,"r+")
    content=f.read()
    #print content
    f.close()
    allurls=[]
    all=re.findall('(http(\S)+)',content,re.I)
    for each in all:
        allurls.append(each[0])
    #print allurls
    return allurls

def get_title_from_uri(uri):
    import mechanize
    import cookielib

    br = mechanize.Browser()
    br.set_cookiejar(cookielib.LWPCookieJar()) # Cookie jar

    br.set_handle_equiv(True) # Browser Option
    br.set_handle_gzip(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)

    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    br.open(uri)
    #print br.title()
    return br.title()

target_allurls=get_uris_from_file(sys.argv[2])

def get_titles():
    writed_urls=[]
    for each in target_allurls:
        f=open("result.txt","a+")
        tmp=urlparse(each)
        http_domain=tmp.scheme+'://'+tmp.hostname
        title=get_title_from_uri(http_domain)
        time.sleep(1)
        try:
            if http_domain not in writed_urls:
                print http_domain
                f.write(http_domain+'\r\n'+'upon uri is:'+title+'\r\n')
                writed_urls.append(http_domain)
        except:
            pass
        f.close()

    
def write_urls_to_file(urls):
    for each in urls:
        f=open("urls.txt","a+")
        f.write(each+"\r\n")
        f.close()
    
write_urls_to_file(target_allurls)
