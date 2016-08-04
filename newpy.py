#############################################################
###
###  mm         .m   mm  '   .
### ' '[. . .m,  ]  .`',.m  .dm
###  .m` b[ ]`T  ]  ] ,[ ]   ]
###   '[ d, ] ]  ]  ]  [ ]   ]
### 'md`.`\ ]bP .dm  bd .dm  'm
###         ]
###         '
###
### name: newpy.py
### function: write new python script easily
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

import os
import datetime
def check_file_has_logo(file_abs_path):
    unsucceed=os.system('''grep -r "import time\\\nfrom exp10it import \*\\\nfiglet2file("3xp10it",2,True)" %s''' % file_abs_path)
    if(unsucceed==1):
        return False
    else:
        return True

def write_code_header_to_file(file_abs_path,function,date,author,blog):
    f=open(file_abs_path,"a+")
    f.write("#############################################################\n")
    f.close()
    figlet2file("3xp10it",file_abs_path,True)
    time.sleep(1)

    f=open(file_abs_path,"a+")
    all=f.readlines()
    f.close()
    f=open("/tmp/1","a+")
    for each in all:
        if(len(each)<61):
            each=each[:-1]+(58-sys.getsizeof(each[:-1]))*' '+'   '
            f.write(each+'\n')
        else:
            f.write(each)
    f.close()
    os.system("rm %s" % file_abs_path)
    os.system("cat /tmp/1 > %s && rm /tmp/1" % file_abs_path)
    #os.system("cat %s" % file_abs_path)

    f=open(file_abs_path,"a+")
    filename=os.path.basename(file_abs_path)

    f.write("###                                                          \n")
    f.write("### name: %s" % filename+(42-len(filename)+6)*' '+'   \n')
    f.write("### function: %s" % function+(38-len(function)+6)*' '+'   \n')
    f.write("### date: %s" % str(date)+(42-len(str(date))+6)*' '+'   \n')
    f.write("### author: %s" % author+(40-len(author)+6)*' '+'   \n')
    f.write("### blog: %s" % blog+(42-len(blog)+6)*' '+'   \n')
    f.write("#############################################################\n")
    f.write('''# -*- coding: utf-8 -*-\nimport sys\nreload(sys)\nsys.setdefaultencoding('utf-8')\n#upon 4 lines for chinese support\nimport time\nfrom exp10it import *\nfiglet2file("3xp10it",2,True)\ntime.sleep(1)\n\n''')
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
    os.system("sed -i 's/### name: newpy.py/### name: %s/g' %s" % (filename,file_abs_path))


def main():
    while 1:
        print "1>write a new script"
        print "2>open and edit a exist script"
        print "your chioce:1/2 default[1]:>",
        num=''
        num==raw_input()
        if(num!=str(2)):
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
            insert_code_header_to_file(file_abs_path,function,date,author,blog)
            break
        else:
            print "please input your file_abs_path to edit:>",
            file_abs_path=raw_input()
            if os.path.exists(file_abs_path) is not True:
                print "file not exist,do you want to edit it and save it as a new file?[y/N] default[N]:>",
                choose=raw_input()
                if choose=='y' or choose=='Y':
                    if(False==check_file_has_logo(file_abs_path)):
                        print "please input the script function:)"
                        function=raw_input()
                        date=datetime.date.today()
                        author="quanyechavshuo"
                        blog="https://3xp10it.github.io"

                        insert_code_header_to_file(file_abs_path,function,date,author,blog)
                        break

                else:
                    continue
            else:
                if(False==check_file_has_logo(file_abs_path)):
                    print "please input the script function:)"
                    function=raw_input()
                    date=datetime.date.today()
                    author="quanyechavshuo"
                    blog="https://3xp10it.github.io"
                    insert_code_header_to_file(file_abs_path,function,date,author,blog)
                    break

    print file_abs_path
    os.system("vim %s" % file_abs_path)
    print "do you want this script upload to github server? Y/n[Y]:"
    choose=raw_input()
    if choose!='n':
        print "please input your remote repository name:)"
        repo_name=raw_input()
        succeed=save2github(file_abs_path,repo_name,function)
        if(succeed==0):
            print "all is done and all is well!!!"

if __name__=='__main__':
    main()
