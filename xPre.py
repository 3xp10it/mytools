import os
import re
import requests
os.system("pip3 install exp10it -U")
from exp10it import get_string_from_command
from exp10it import get_request
#下面设置zsh为默认shell
os.system("chsh -s `which zsh`")
#下面安装oh-my-zsh
os.system('''sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"''')
a=get_string_from_command("uname -a")
if re.search(r"(debian)|(ubuntu)",a,re.I):
    #下面安装.zshrc配置
    os.system("cd && wget https://raw.githubusercontent.com/3xp10it/.zshrc/master/.zshrc_ubuntu -O .zshrc")
    #下面准备配置ctrl与caps键,其中上面的.zshrc中已经有caps设置按住为ctrl,按一下为esc
    os.system("apt-get install xcape")
    #下面安装tmux
    os.system("apt-get install tmux")
    #下面安装tmux配置
    os.system("cd && wget https://raw.githubusercontent.com/3xp10it/.tmux/master/ubuntuTmux/.tmux.conf && wget https://raw.githubusercontent.com/3xp10it/.tmux/master/ubuntuTmux/.tmux.conf.local")
    #下面安装较新版本vim
    os.system("apt-get install vim")
    #下面安装vim配置
    os.system("cd && wget https://raw.githubusercontent.com/3xp10it/.vimrc/master/.vimrc_linux -O .vimrc")
    #下面安装vim的vundle插件管理工具
    os.system("git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim")
    input("1.I have download vundle for you,you need open a new terminal and run vim and :BundleInsall by yourself,then press any key")
    #下面安装vimperator配置
    os.system("cd && wget https://raw.githubusercontent.com/3xp10it/.vimrc/master/.vimperatorrc_linux -O .vimperatorrc")
    input("2.I have download vimperatorrc for you,you need install vimperator in firefox by yourself,then press any key")

elif re.search(r"darwin",a,re.I):
    os.system("cd && wget https://raw.githubusercontent.com/3xp10it/.zshrc/master/.zshrc_macOS -O .zshrc")
    #下面安装最新版本tmux
    html=requests.get("https://github.com/tmux/tmux/releases").text
    a=re.findall(r'''href="(.*\.tar.gz)"''',html,re.I)
    tmuxUrl="https://github.com"+a[0]
    os.system("wget %s -O /tmp/tmux.tar.gz" % tmuxUrl)
    os.system("cd /tmp && tar -xvzf tmux.tar.gz -C /tmp/tmux")
    os.system("cd /tmp/tmux && ./configure && make && make install && rm -r /tmp/tmux && rm /tmp/tmux.tar.gz")
    #下面安装tmux配置
    os.system("cd && wget https://raw.githubusercontent.com/3xp10it/.tmux/master/macosTmux/.tmux.conf && wget https://raw.githubusercontent.com/3xp10it/.tmux/master/macosTmux/.tmux.conf.local")
    #下面安装最新版本macvim
    html=requests.get("https://github.com/macvim-dev/macvim/releases/").text
    a=re.findall(r'''href="(.*\.dmg)"''',html,re.I)
    macvimUrl="https://github.com"+a[0]
    os.system("wget %s -O /tmp/MacVim.dmg" % macvimUrl)
    os.system("open /tmp/MacVim.dmg")
    #下面安装vim配置
    os.system("cd && wget https://raw.githubusercontent.com/3xp10it/.vimrc/master/.vimrc_MacVim -O .vimrc")
    #下面安装vim的vundle插件管理工具
    os.system("git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim")
    print("1.I have download vundle for you,you need run vim and :BundleInsall by yourself")
    #下面安装vimperator配置
    os.system("cd && wget https://raw.githubusercontent.com/3xp10it/.vimrc/master/.vimperatorrc_macOS -O .vimperatorrc")
    print("2.I have download vimperatorrc for you,you need install vimperator in firefox by yourself")

print("Congratulations! zsh & tmux & vim are ok for work now")
