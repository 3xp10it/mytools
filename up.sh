if [ -f ~/.bashrc ]; then
    . ~/.bashrc
fi

if [ -d ~/myblog ] && [ -d ~/3xp10it.github.io ]
then
    cd ~/myblog && cp index_bak.html index.html && (rm -r _site/ || true) && jekyll serve --incremental --watch && cp _site/index.html index2.html && cp bak.html index.html && echo -e "\033[31m congratulations! generate new _site content finished. \033[0m"
    cd ~/3xp10it.github.io && (rm -r * || true) && cp -r ../myblog/_site/* . && cp ../myblog/index2.html . && cp ../myblog/index.html . && git status && git add . && git commit -a -m "update" && git push -u origin master && echo -e "\033[31m congratulations! upload 3xp10it.github.io finished. \033[0m"
    cd ~/myblog && git status && git add . && git commit -a -m "update backup" && git push -u origin master && echo -e "\033[31m upload myblog finished. \033[0m"
else
    echo "this is the first time you use me,I will download myblog from https://github.com/3xp10it/myblog.git"
    mkdir ~/myblog && cd ~/myblog && git init && git pull https://github.com/3xp10it/myblog.git && git remote add origin https://github.com/3xp10it/myblog.git
    echo "this is the first time you use me,I will download 3xp10it.github.io from https://github.com/3xp10it/3xp10it.github.io.git"
    #mkdir ~/3xp10it.github.io && cd ~/3xp10it.github.io && git init && git pull https://github.com/3xp10it/3xp10it.github.io.git && git remote add origin https://github.com/3xp10it/3xp10it.github.io.git
    cd && git clone https://github.com/3xp10it/3xp10it.github.io.git 
fi

