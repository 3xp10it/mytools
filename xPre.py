import os
import re
import requests
from exp10it import get_string_from_command
a=get_string_from_command("pip3")
if re.search(r"(未找到命令)|(command not found)",a,re.I):
    os.system("apt-get install python3-pip")
os.system("pip3 install exp10it -U")
from exp10it import get_request
sysinfo = get_string_from_command("uname -a")

# 安装git,为了后面能安装vundle
a=get_string_from_command("git help")
if re.search(r"(未找到命令)|(not found)|(unknown command)",a,re.I):
    if re.search(r"(ubuntu)|(debain)",sysinfo,re.I):
        os.system("echo y | apt-get install git")
    if re.search(r"darwin",sysinfo,re.I):
        os.system("brew install git")

with open("/etc/shells", "r") as f:
    content = f.read()
pur = input("1.只更新配置文件\n2.安装zsh+vim+tmux+配置文件\n3.安装fish+vim+tmux+配置文件\ninput your choose here:>")
if pur == '1':
    pass
elif pur == '2':
    # 下面设置zsh为默认shell
    if not os.path.exists("/bin/zsh"):
        os.system("echo y | apt-get install zsh")
    if not re.search(r"/bin/zsh", content, re.I):
        os.system('''echo "/bin/zsh" | sudo tee -a /etc/shells''')
    os.system("chsh -s `which zsh`")
    # 下面安装oh-my-zsh
    os.system('''sh -c "$(curl -fs_sL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)" && exit''')
    # 上面之后要退出zsh,要不然后续的安装过程无法继续(除非人工ctrl+d)

else:
    # 选择3(安装fish）
    # 下面设置fish为默认shell
    if re.search(r"(debian)|(ubuntu)", sysinfo, re.I):
        os.system("echo 'deb http://download.opensuse.org/repositories/shells:/fish:/release:/2/Debian_9.0/ /' > /etc/apt/sources.list.d/fish.list ")
        os.system("echo y | apt-get update")
        os.system("echo y | apt-get install fish")
    elif re.search(r"darwin",sysinfo,re.I):
        os.system("brew install fish")
    if not re.search(r"/usr/local/bin/fish", content, re.I):
        os.system('''echo "/usr/local/bin/fish" | sudo tee -a /etc/shells''')
    os.system("chsh -s `which fish`")
    # 下面安装oh-my-fish
    os.system('''curl -L https://get.oh-my.fish | fish''')
    # 上面之后要退出fish,要不然后续的安装过程无法继续(除非人工ctrl+d)


if re.search(r"(debian)|(ubuntu)", sysinfo, re.I):
    # 下面安装.zshrc配置
    os.system("cd && wget https://github.com/3xp10it/config/raw/master/.zshrc/.zshrc_ubuntu -O .zshrc")
    # 下面安装config.fish配置
    os.system("wget https://github.com/3xp10it/config/raw/master/config.fish/config.fish -O ~/.config/fish/config.fish")
    if pur == '1':
        pass
    else:
        # 下面准备配置ctrl与caps键,其中上面的.zshrc中已经有caps设置按住为ctrl,按一下为esc
        os.system("echo y | apt-get install xcape")
        # 下面安装tmux
        os.system("echo y | apt-get install tmux")
    # 下面安装tmux配置
    os.system("cd && wget https://github.com/3xp10it/config/raw/master/.tmux/ubuntuTmux/.tmux.conf -O .tmux.conf && wget https://github.com/3xp10it/config/raw/master/.tmux/ubuntuTmux/.tmux.conf.local -O .tmux.conf.local")

    if pur == "1":
        pass
    else:
        # 下面安装较新版本vim
        os.system("echo y | apt-get install software-properties-common && add-apt-repository ppa:jonathonf/vim && apt update && apt install vim")
    # 下面安装vim配置
    os.system("cd && wget https://github.com/3xp10it/config/raw/master/.vimrc/.vimrc_linux -O .vimrc")

    if pur == '1':
        pass
    else:
        # 下面安装vim的vundle插件管理工具
        os.system("git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim")
        input("1.I have download vundle for you,you need open a new terminal and run vim and :BundleInsall by yourself,then press any key")
    # 下面安装vimperator配置
    os.system("cd && wget https://github.com/3xp10it/config/raw/master/.vimrc/.vimperatorrc_linux -O .vimperatorrc")

    if pur == '1':
        pass
    else:
        input("2.I have download vimperatorrc for you,you need install vimperator in firefox by yourself,then press any key")

    # 下面更新rime配置
    os.system("wget https://raw.githubusercontent.com/3xp10it/AutoIM/master/default.custom.yaml -O ~/.config/ibus/rime/default.custom.yaml")
    input("如果安装了rime,此时需要重新部署rime,然后按任意键继续...")

elif re.search(r"darwin", sysinfo, re.I):
    # 下面安装.zshrc配置文件
    os.system("cd && wget https://github.com/3xp10it/config/raw/master/.zshrc/.zshrc_macOS -O .zshrc")
    # 下面安装config.fish配置
    os.system("wget https://github.com/3xp10it/config/raw/master/config.fish/config.fish -O ~/.config/fish/config.fish")
    if pur == '1':
        pass
    else:
        # 下面安装最新版本tmux
        html = requests.get("https://github.com/tmux/tmux/releases").text
        a = re.findall(r'''href="(.*\.tar.gz)"''', html, re.I)
        tmux_url = "https://github.com" + a[0]
        os.system("wget %s -O /tmp/tmux.tar.gz" % tmux_url)
        os.system("cd /tmp && tar -xvzf tmux.tar.gz -C /tmp/tmux")
        os.system("cd /tmp/tmux && ./configure && make && make install && rm -r /tmp/tmux && rm /tmp/tmux.tar.gz")
    # 下面安装tmux配置
    os.system("cd && wget https://github.com/3xp10it/config/raw/master/.tmux/macosTmux/.tmux.conf -O .tmux.conf && wget https://github.com/3xp10it/config/raw/master/.tmux/macosTmux/.tmux.conf.local -O .tmux.conf.local")
    if pur == '1':
        pass
    else:
        # 下面安装最新版本macvim
        html = requests.get("https://github.com/macvim-dev/macvim/releases/").text
        a = re.findall(r'''href="(.*\.dmg)"''', html, re.I)
        macvim_url = "https://github.com" + a[0]
        os.system("wget %s -O /tmp/MacVim.dmg" % macvim_url)
        os.system("open /tmp/MacVim.dmg")
    # 下面安装vim配置
    os.system("cd && wget https://github.com/3xp10it/config/raw/master/.vimrc/.vimrc_MacVim -O .vimrc")

    if pur == '1':
        pass
    else:
        # 下面安装vim的vundle插件管理工具
        os.system("git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim")
        print("1.I have download vundle for you,you need run vim and :BundleInsall by yourself")
    # 下面安装vimperator配置
    os.system("cd && wget https://github.com/3xp10it/config/raw/master/.vimrc/.vimperatorrc_macOS -O .vimperatorrc")

    if pur == '1':
        pass
    else:
        input("2.I have download vimperatorrc for you,you need install vimperator in firefox by yourself,then press any key")

    # 下面更新squirrel配置
    os.system("wget https://raw.githubusercontent.com/3xp10it/AutoIM/master/default.custom.yaml -O ~/Library/Rime/default.custom.yaml")
    input("如果安装了squirrel,此时需要重新部署squirrel,然后按任意键继续...")

print("Congratulations! All your work has been finished:)")
