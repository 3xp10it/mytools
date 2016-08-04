#############################################################
###  ___           ,  __
### /   \         /| /  \ o
###   __/       _  ||    |  _|_
###     \/\/  |/ \_||    ||  |
### \___/ /\_/|__/ | \__/ |_/|_/
###          /|
###          \|
###
### name: 2
### function: a test for other file
### date: 2016-08-04
### author: quanyechavshuo
### blog: https://3xp10it.github.io
#############################################################
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#upon 4 lines for chinese support
import time
from exp10it import *
figlet2file("3xp10it",2,True)
time.sleep(1)

# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#必须加上上面四行,否则各种编码的错误爆出

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
    unsucceed=os.system("figlet -t -f %s %s > /tmp/1" % (random_font,logo_str))
    if(unsucceed==1):
        print "something wrong with figlet,check the command in python source file"
    try:
        f=open("/tmp/1","r+")
        all=f.readlines()
        f.close()
        f=open(file_abs_path,"a+")
        for each in all:
            f.write("### "+each)
        f.close()
    except:
        pass
    if(print_or_not==True):
        os.system("cat /tmp/1")
    os.system("rm /tmp/1")

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
#由于此处tmp和all_file_name_list在函数外面,so
#在其他代码中调用get_all_file_name()时要用from name import *,不用import name,否则不能调用到get_all_file_name的功能
tmp=0
all_file_name_list=[]
def get_all_file_name(folder,ext_list):
    global tmp
    global root_dir
    global all_file_name_list
    tmp+=1
    if tmp==1:
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
                for each_ext in ext_list:
                    if(filename.split('.')[-1]==each_ext):
                        #print filename
                        all_file_name_list.append(filename)
            else:
                #print each
                for each_ext in ext_list:
                    if(each.split('.')[-1]==each_ext):
                        #print each
                        all_file_name_list.append(each)

    return all_file_name_list


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
        os.system("cp %s %s" % (file_abs_path,local_resp_path))
        succeed=os.system("cd %s && git add . && git status && git commit -a -m '%s' && git push -u origin master" % (local_resp_path,comment))
        if(succeed==0):
            print "push succeed!!!"
            return True
        else:
            print "push to git wrong,wrong,wrong,check it!!!"
            return False

    if os.path.exists(local_resp_path) is True and os.path.exists(local_resp_path+"/.git") is False:
        os.system("mkdir /tmp/codetmp")
        os.system("cd %s && cp -r * /tmp/codetmp/ && git init && git pull %s" % (local_resp_path,remote_resp_uri))
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
        if os.path.exists(local_resp_path+"/"+filename) is True:
            print "warning!warning!warning! I will exit! There exists a same name script in local_resp_path(>>%s),you should rename your script if you want to upload it to git:)" % local_resp_path+"/"+filename
            return False
        os.system("cp %s %s" % (file_abs_path,local_resp_path))
        succeed=os.system("cd %s && git add . && git status && git commit -a -m '%s' && git push -u origin master" % (local_resp_path,comment))
        if(succeed==0):
            print "push succeed!!!"
            return True
        else:
            print "push to git wrong,wrong,wrong,check it!!!"
            return False

