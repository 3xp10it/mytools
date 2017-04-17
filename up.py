import os
homePath=os.path.expanduser("~")
if os.path.exists(homePath+'/myblog') is False and os.path.exists(homePath+'/3xp10it.github.io') is False:
    print "this is the first time you use me,I will download myblog from https://github.com/3xp10it/myblog.git"
    os.system("mkdir ~/myblog && cd ~/myblog && git init && git pull https://github.com/3xp10it/myblog.git && git remote add origin https://github.com/3xp10it/myblog.git")
    print "this is the first time you use me,I will download 3xp10it.github.io from https://github.com/3xp10it/3xp10it.github.io.git"
    os.system("mkdir ~/3xp10it.github.io && cd ~/3xp10it.github.io && git init && git pull https://github.com/3xp10it/3xp10it.github.io.git && git remote add origin https://github.com/3xp10it/3xp10it.github.io.git")
else:
    os.system('''cd ~/myblog && pkill jekyll;pkill ruby;sleep 3 && cp index.html tmp.html && cp index_bak.html index.html && sh -c "rm -r _site/ & jekyll serve --watch & sleep 3 && exit" && cp _site/index.html index2.html && cp tmp.html index.html && echo congratulations! commands execute ok to here!''')
    os.system('''cd ~/3xp10it.github.io && cp -r ../myblog/_site/* . && cp ../myblog/index2.html . && cp ../myblog/index.html . && git status && git add . && git status && git commit -a -m "update" && git push -u origin master && echo congratulations! commands execute ok to here!''')
    os.system('''cd ~/myblog && git status && git add . && git status && git commit -a -m "update backup" && git push -u origin master && echo all is well,and all is done!''')

