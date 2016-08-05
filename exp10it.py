#############################################################
### ___ /           _ |  _ \ _) |
###   _ \\ \  / __ \  | |   | | __|
###    ) |`  <  |   | | |   | | |
### ____/ _/\_\ .__/ _|\___/ _|\__|
###            _|
###
### name: exp10it.py
### function: my module
### date: 2016-08-05
### author: quanyechavshuo
### blog: https://3xp10it.github.io
#############################################################
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#upon 4 lines for chinese support

import os
import re
import random

def figlet2file(logo_str,file_abs_path,print_or_not):
    #输出随机的logo文字到文件或屏幕,第二个参数为任意非文件的参数时(eg.0,1,2),只输出到屏幕
    #apt-get install figlet
    #man figlet
    #figure out which is the figlet's font directory
    #my figlet font directory is:
    #figlet -I 2,output:/usr/share/figlet

    try:
        f=os.popen("figlet -I 2")
        all=f.readlines()
        f.close()
        figlet_font_dir=all[0][:-1]
    except:
        os.system("apt-get install figlet")
        f=os.popen("figlet -I 2")
        all=f.readlines()
        f.close()
        figlet_font_dir=all[0][:-1]

    all_font_name_list=get_all_file_name(figlet_font_dir,['tlf','flf'])
    random_font=random.choice(all_font_name_list)
    unsucceed=os.system("figlet -t -f %s %s > /tmp/3" % (random_font,logo_str))
    if(unsucceed==1):
        print "something wrong with figlet,check the command in python source file"
    try:
        os.system("cat /tmp/3 >> %s" % file_abs_path)
    except:
        pass
    if(print_or_not==True):
        os.system("cat /tmp/3")
    os.system("rm /tmp/3")

def oneline2nline(oneline,nline,file_abs_path):
    #将文件中的一行字符串用多行字符串替换，调用时要将"多行字符串的参数(第二个参数)"中的换行符设置为\n
    tmpstr=nline.replace('\n','\\\n')
    os.system("sed '/%s/c\\\n%s' %s > /tmp/1" % (oneline,tmpstr,file_abs_path))
    os.system("cat /tmp/1 > %s && rm /tmp/1" % file_abs_path)
    pass

def lin2win(file_abs_path):
    #将linux下的文件中的\n换行符换成win下的\n\n换行符
    import sys
    input_file=file_abs_path
    f=open(input_file,"r+")
    urls=f.readlines()
    f.close()
    os.system("rm %s" % file_abs_path)
    f1=open(file_abs_path,"a+")
    for url in urls:
    	print url[0:-1]
    	#print url is different with print url[0:-1]
    	#print url[0:-1] can get the pure string
    	#while print url will get the "unseen \n"
    	#this script can turn a file with strings
    	#end with \n into a file with strings end
    	#with \r\n to make it comfortable move the
    	#txt file from *nix to win,coz the file with
    	#strings end with \n in *nix is ok for human
    	#to see "different lines",but this kind of file
    	#will turn "unsee different lines" in win
    	f1.write(url[0:-1]+"\r\n")
    f1.close()


#attention:
#由于此处tmp_get_file_name_value和tmp_all_file_name_list在函数外面,so
#在其他代码中调用get_all_file_name()时要用from name import *,不用import name,否则不能调用到get_all_file_name的功能
tmp_get_file_name_value=0
tmp_all_file_name_list=[]
def get_all_file_name(folder,ext_list):
    #exp_list为空时，得到目录下的所有文件名,不返回空文件夹名
    #返回结果为文件名列表，不是完全绝对路径名
    #eg.folder="/root"时，当/root目录下有一个文件夹a，一个文件2.txt,a中有一个文件1.txt
    #得到的函数返回值为['a/1.txt','2.txt']
    global tmp_get_file_name_value
    global root_dir
    global tmp_all_file_name_list
    tmp_get_file_name_value+=1
    if tmp_get_file_name_value==1:
        if folder[-1]=='/':
            root_dir=folder[:-1]
        else:
            root_dir=folder

    allfile=os.listdir(folder)
    for each in allfile:
        each_abspath=os.path.join(folder,each)
        if os.path.isdir(each_abspath):
            get_all_file_name(each_abspath,ext_list)
        else:
            #print each_abspath
            if len(each_abspath)>len(root_dir)+1+len(os.path.basename(each)):
                filename=each_abspath[len(root_dir)+1:]
                #print filename
                if len(ext_list)==0:
                    tmp_all_file_name_list.append(filename)
                else:
                    for each_ext in ext_list:
                        if(filename.split('.')[-1]==each_ext):
                            #print filename
                            tmp_all_file_name_list.append(filename)
            else:
                #print each
                if len(ext_list)==0:
                    tmp_all_file_name_list.append(each)
                else:
                    for each_ext in ext_list:
                        if(each.split('.')[-1]==each_ext):
                            #print each
                            tmp_all_file_name_list.append(each)

    return tmp_all_file_name_list


def save2github(file_abs_path,repo_name,comment):
    #将文件上传到github
    #arg1:文件绝对路经
    #arg2:远程仓库名
    #提交的commit注释
    local_resp_path="/root/"+repo_name
    filename=os.path.basename(file_abs_path)
    remote_resp_uri="https://github.com/3xp10it/%s.git" % repo_name
    if os.path.exists(local_resp_path) is False:
        os.system("mkdir %s && cd %s && git init && git pull %s && git remote add origin %s && git status" % (local_resp_path,local_resp_path,remote_resp_uri,remote_resp_uri))
        if os.path.exists(local_resp_path+"/"+filename) is True:
            print "warning!warning!warning! I will exit! There exists a same name script in local_resp_path(>>%s),and this script is downloaded from remote github repo,you should rename your script if you want to upload it to git:)" % local_resp_path+"/"+filename
            return False
        os.system("cp %s %s" % (file_abs_path,local_resp_path))
        succeed=os.system("cd %s && git add . && git status && git commit -a -m '%s' && git push -u origin master" % (local_resp_path,comment))
        if(succeed==0):
            print "push succeed!!!"
            return True
        else:
            print "push to git wrong,wrong,wrong,check it!!!"
            return False

    if os.path.exists(local_resp_path) is True and os.path.exists(local_resp_path+"/.git") is False:
        if os.path.exists(local_resp_path+"/"+filename) is True:
            print "warning!warning!warning! I will exit! There exists a same name script in local_resp_path(>>%s),you should rename your script if you want to upload it to git:)" % local_resp_path+"/"+filename
            return False
        os.system("mkdir /tmp/codetmp")
        os.system("cd %s && cp -r * /tmp/codetmp/ && rm -r * &&  git init && git pull %s" % (local_resp_path,remote_resp_uri))
        os.system("cp -r /tmp/codetmp/* %s && rm -r /tmp/codetmp" % local_resp_path)
        os.system("cp %s %s" % (file_abs_path,local_resp_path))
        succeed=os.system("cd %s && git add . && git status && git commit -a -m '%s' && git remote add origin %s && git push -u origin master" % (local_resp_path,comment,remote_resp_uri))
        if(succeed==0):
            print "push succeed!!!"
            return True
        else:
            print "push to git wrong,wrong,wrong,check it!!!"
            return False

    if os.path.exists(local_resp_path) is True and os.path.exists(local_resp_path+"/.git") is True:
        #如果本地local_resp_path存在，且文件夹中有.git,当local_resp_path文件夹中的文件与远程github仓库中的文件不一致时，
        #且远程仓库有本地仓库没有的文件，选择合并本地和远程仓库并入远程仓库,所以这里采用一并重新合并的处理方法，
        #(与上一个if中的情况相比，多了一个合并前先删除本地仓库中的.git文件夹的动作),
        #虽然当远程仓库中不含本地仓库没有的文件时，不用这么做，但是这样做也可以处理那种情况
        if os.path.exists(local_resp_path+"/"+filename) is True:
            print "warning!warning!warning! I will exit! There exists a same name script in local_resp_path(>>%s),you should rename your script if you want to upload it to git:)" % local_resp_path+"/"+filename
            return False
        os.system("cd %s && rm -r .git" % local_resp_path)
        os.system("mkdir /tmp/codetmp")
        os.system("cd %s && cp -r * /tmp/codetmp/ && rm -r * && git init && git pull %s" % (local_resp_path,remote_resp_uri))
        os.system("cp -r /tmp/codetmp/* %s && rm -r /tmp/codetmp" % local_resp_path)
        os.system("cp %s %s" % (file_abs_path,local_resp_path))
        succeed=os.system("cd %s && git add . && git status && git commit -a -m '%s' && git remote add origin %s && git push -u origin master" % (local_resp_path,comment,remote_resp_uri))
        if(succeed==0):
            print "push succeed!!!"
            return True
        else:
            print "push to git wrong,wrong,wrong,check it!!!"
            return False


#below code are the function about tab key complete with file path
#------------------------start-of-key-complete-with-file-path--------------------------------
import os
import sys
import readline
import glob
class tabCompleter(object):
        """
        A tab completer that can either complete from
        the filesystem or from a list.
        Partially taken from:
        http://stackoverflow.com/questions/5637124/tab-completion-in-pythons-raw-input
        source code:https://gist.github.com/iamatypeofwalrus/5637895
        """

        def pathCompleter(self,text,state):
            """
            This is the tab completer for systems paths.
            Only tested on *nix systems
            """
            line   = readline.get_line_buffer().split()
            return [x for x in glob.glob(text+'*')][state]

        def createListCompleter(self,ll):
            """
            This is a closure that creates a method that autocompletes from
            the given list.
            Since the autocomplete function can't be given a list to complete from
            a closure is used to create the listCompleter function with a list to complete
            from.
            """
            def listCompleter(text,state):
                line   = readline.get_line_buffer()
                if not line:
                    return [c + " " for c in ll][state]
                else:
                    return [c + " " for c in ll if c.startswith(line)][state]
            self.listCompleter = listCompleter
t = tabCompleter()
t.createListCompleter(["ab","aa","bcd","bdf"])

readline.set_completer_delims('\t')
readline.parse_and_bind("tab: complete")
#readline.set_completer(t.listCompleter)
#ans = raw_input("Complete from list ")
#print ans
readline.set_completer(t.pathCompleter)
#--------------------------end-of-key-complete-with-file-path--------------------------------

def get_title_from_uri(uri):
    #得到uri对应的title
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

def get_uris_from_file(file):
    #从文件中获取所有uri
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

def get_title_from_file(file):
    #等到文件中的所有uri对应的title
    target_allurls=get_uris_from_file(file)
    print "a output file:/tmp/result.txt"
    writed_urls=[]
    for each in target_allurls:
        f=open("/tmp/result.txt","a+")
        tmp=urlparse(each)
        http_domain=tmp.scheme+'://'+tmp.hostname
        title=get_title_from_uri(http_domain)
        time.sleep(1)
        try:
            if http_domain not in writed_urls:
                each_line_to_write=http_domain+'\r\n'+'upon uri is:'+title+'\r\n'
                print each_line_to_write
                f.write(each_line_to_write)
                writed_urls.append(http_domain)
        except:
            pass
    f.close()
