if [ -d ~/myblog ] && [ -d ~/3xp10it.github.io ]
then
    cd ~/myblog && cp index.html tmp.html && cp index_bak.html index.html && sh -c "rm -r _site/ & jekyll serve --incremental --watch && exit" && cp _site/index.html index2.html && cp tmp.html index.html && echo congratulations! generate new _site content finished.
    cd ~/3xp10it.github.io && cp -r ../myblog/_site/* . && cp ../myblog/index2.html . && cp ../myblog/index.html . && git status && git add . && git commit -a -m "update" && git push -u origin master && echo congratulations! upload 3xp10it.github.io finished.
    cd ~/myblog && git status && git add . && git commit -a -m "update backup" && git push -u origin master && echo upload myblog finished.
else
    echo "this is the first time you use me,I will download myblog from https://github.com/3xp10it/myblog.git"
    mkdir ~/myblog && cd ~/myblog && git init && git pull https://github.com/3xp10it/myblog.git && git remote add origin https://github.com/3xp10it/myblog.git
    echo "this is the first time you use me,I will download 3xp10it.github.io from https://github.com/3xp10it/3xp10it.github.io.git"
    mkdir ~/3xp10it.github.io && cd ~/3xp10it.github.io && git init && git pull https://github.com/3xp10it/3xp10it.github.io.git && git remote add origin https://github.com/3xp10it/3xp10it.github.io.git
fi

