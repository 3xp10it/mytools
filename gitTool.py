# 每天第1次接触电脑时运行py3 gitTool.py --update
# 每天第-1次接触电脑时运行py3 gitTool.py --commit

import sys
import os
dirList = ["~/myblog/", "~/3xp10it.github.io/",
           "~/mypypi/", "/usr/share/mytools","~/githubpic/"]
if sys.argv[1] == "--update":
    for eachDir in dirList:
        os.system("cd %s && git pull" % eachDir)
if sys.argv[1] == "--commit":
    os.system("bash /usr/share/mytools/up.sh")
    for eachDir in dirList:
        os.system(
            "cd %s && git add . && git commit -a -m 'up' && git push -u origin master" % eachDir)
