import sys
import os
from exp10it import getHomePath

tmp=0
all_file_name_list=[]
def get_all_file_name(folder):
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
            get_all_file_name(each_abspath)
        else:
            #print each_abspath
            if len(each_abspath)>len(root_dir)+1+len(os.path.basename(each)):
                filename=each_abspath[len(root_dir)+1:]
                #print filename
                all_file_name_list.append(filename)
            else:
                #print each
                all_file_name_list.append(each)

    return all_file_name_list


def main():
    homePath=getHomePath()
    githubpicPath=homePath+"/githubpic"
    if os.path.exists(githubpicPath) is False:
        print("this is the first time you use me,or you have deleted ~/githubpic,I will mkdir ~/githubpic and git pull the github's pic.git,please put pngs to ~/githubpic when needed,and don't delet any png file in this folder")
        os.system("mkdir ~/githubpic && cd ~/githubpic && git init && git pull https://github.com/3xp10it/pic.git && git remote add origin https://github.com/3xp10it/pic.git && git status")
        return

    os.system("cd ~/githubpic && git add . && git status && git commit -a -m 'update' && git push -u origin master")

    all_png_list=get_all_file_name(githubpicPath)

    for each in all_png_list:
        if each[-3:]=='png':
            try:
                addressPath=githubpicPath+"/address.txt"
                f=open(addressPath,"a+")
                all=f.readlines()
                each_addr="https://raw.githubusercontent.com/3xp10it/pic/master/%s" % each
                if each_addr+'\r\n' not in all:
                    print(each_addr)
                    f.write(each_addr+'\r\n')
                    f.close()
            except:
                print("open ~/githubpic/address.txt wrong")

if __name__=='__main__':
    main()


'''
print os.path.abspath(each) is not good function,

it will get ~/桌面/spider_wooyun when I put this py script file in ~/桌面,and run:
(cd 桌面)
python mysnippingtool.py
it will get "~/桌面/spider_wooyun" as a result,but the true result should be "~/githubpic/spider_wooyun"
so I use:
current_file_abspath=os.path.isdir("~/githubpic/"+each):
to get the current file's abspath
'''




