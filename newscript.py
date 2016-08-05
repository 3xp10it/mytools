#############################################################
###
###  mm,            .m   .m,   W
### ]""W,           PW   W"W   "   ][
###    d['W W`]bWb   W  ][ ][ WW  ]WWW
###  ]WW  ]W[ ]P T[  W  ][W][  W   ][
###    T[ .W, ][ ][  W  ][ ][  W   ][
### ]mmW` d"b ]WmW`.mWm, WmW .mWm, ]bm
###  ""` '" "`]["` '"""` '"` '"""`  ""
###           ][
###
###
### name: newscript.py
### function: write new script easily
### date: 2016-08-05
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
figlet2file("3xp10it","/tmp/figletpic",True)
time.sleep(1)


import os
import datetime
def check_file_has_logo(file_abs_path):
    unsucceed=os.system('''grep -r "### blog: https://3xp10it.github.io" %s''' % file_abs_path)
    if(unsucceed==1):
        return False
    else:
        return True

def write_code_header_to_file(file_abs_path,function,date,author,blog):
    f=open(file_abs_path,"a+")
    first_line="#############################################################\n"
    f.write(first_line)
    f.close()
    figlet2file("3xp10it",file_abs_path,False)
    f=open(file_abs_path,"a+")
    all=f.readlines()
    f.close()
    f=open("/tmp/1","a+")
    for each in all:
        if(each[0:40]!="#"*40):
            f.write("### "+each)
        else:
            f.write(each)
    f.close()
    os.system("cat /tmp/1 > %s && rm /tmp/1" % file_abs_path)
    #os.system("cat %s" % file_abs_path)

    f=open(file_abs_path,"a+")
    filename=os.path.basename(file_abs_path)

    f.write("###                                                          \n")
    f.write("### name: %s" % filename+'\n')
    f.write("### function: %s" % function+'\n')
    f.write("### date: %s" % str(date)+'\n')
    f.write("### author: %s" % author+'\n')
    f.write("### blog: %s" % blog+'\n')
    f.write("#############################################################\n")
    if file_abs_path.split(".")[-1]=='py':
        f.write('''# -*- coding: utf-8 -*-\nimport sys\nreload(sys)\nsys.setdefaultencoding('utf-8')\n#upon 4 lines for chinese support\nimport time\nfrom exp10it import *\nfiglet2file("3xp10it","/tmp/figletpic",True)\ntime.sleep(1)\n\n''')
    f.close()

def insert_code_header_to_file(file_abs_path,function,date,author,blog):
    all_lines=[]
    f=open(file_abs_path,"a+")
    all_lines=f.readlines()
    f.close()
    write_code_header_to_file("/tmp/2",function,date,author,blog)
    f=open("/tmp/2","a+")
    for each in all_lines:
        f.write(each)
    f.close()
    os.system("cat /tmp/2 > %s && rm /tmp/2" % file_abs_path)
    filename=os.path.basename(file_abs_path)
    os.system("sed -i 's/### name: %s/### name: %s/g' %s" % ('2',filename,file_abs_path))


def main():
    while 1:
        print "1>write a new script"
        print "2>open and edit a exist script"
        print "your chioce:1/2 default[1]:>",
        tmp=raw_input()
        if(tmp!=str(2)):
            print "please input your file_abs_path:>",
            file_abs_path=raw_input()
            if(os.path.exists(file_abs_path)==True):
                print "file name exists,u need to change the file name,or if you really want the name,it will replace the original file!!!"
                print "replace the original file? Or you want to edit(e/E for edit) the file direcly?"
                print " y/n/e[N]:>",
                choose=raw_input()
                if(choose!='y' and choose!='Y' and choose!='e' and choose!='E'):
                    continue
                elif(choose=='y' or choose=='Y'):
                    os.system("rm %s" % file_abs_path)
                    print "please input the script function:)"
                    function=raw_input()
                    date=datetime.date.today()
                    author="quanyechavshuo"
                    blog="https://3xp10it.github.io"

                    insert_code_header_to_file(file_abs_path,function,date,author,blog)

                    break
            print "please input the script function:)"
            function=raw_input()
            date=datetime.date.today()
            author="quanyechavshuo"
            blog="https://3xp10it.github.io"
            if os.path.basename(file_abs_path)!="newscript.py" and "exp10it.py"!=os.path.basename(file_abs_path):
                insert_code_header_to_file(file_abs_path,function,date,author,blog)
            break
        else:
            print "please input your file_abs_path to edit:>",
            file_abs_path=raw_input()
            if os.path.exists(file_abs_path) is False:
                print "file not exist,do you want to edit it and save it as a new file?[y/N] default[N]:>",
                choose=raw_input()
                if choose=='y' or choose=='Y':
                    if("exp10it.py"!=os.path.basename(file_abs_path)):
                        print "please input the script function:)"
                        function=raw_input()
                        date=datetime.date.today()
                        author="quanyechavshuo"
                        blog="https://3xp10it.github.io"

                        insert_code_header_to_file(file_abs_path,function,date,author,blog)
                        break
                    else:
                        print "warning! you are edit a new file named 'exp10it',this is special,you know it's your python module's name,so I will exit:)"


                else:
                    continue
            else:
                if(False==check_file_has_logo(file_abs_path) and "exp10it.py"!=os.path.basename(file_abs_path) and "newscript.py"!=os.path.basename(file_abs_path)):
                    print "please input the script function:)"
                    function=raw_input()
                    date=datetime.date.today()
                    author="quanyechavshuo"
                    blog="https://3xp10it.github.io"
                    insert_code_header_to_file(file_abs_path,function,date,author,blog)
                    break
                else:
                    break

    os.system("vim %s" % file_abs_path)
    print "do you want this script upload to github server? Y/n[Y]:"
    choose=raw_input()
    if choose!='n':
        print "please input your remote repository name:)"
        repo_name=raw_input()
        succeed=save2github(file_abs_path,repo_name,function)
        if(succeed==True):
            print "all is done and all is well!!!"
        else:
            print "save2github wrong,check it,maybe your remote repository name input wrong..."

def get_folder_name(folder_path):
    print os.listdir(folder_path)

if __name__=='__main__':
    main()
