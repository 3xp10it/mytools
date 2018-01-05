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
### name: macosbak.sh
### function: bakup system
### date: 2017-03-17
### author: quanyechavshuo
### blog: http://3xp10it.cc
#############################################################
#macos系统备份脚本，备份产生两个文件,macosbak2.tgz为最新备份文件,macosbak1.tgz为上一次备份的文件
# crontab -e like：
# m h  dom mon dow   command
#18  8    5 * *   root    bash ~/mytools/macosbak.sh

bakupdevice="/"
bakupfolder="/macosbak/"
bakupfile1="/macosbak/macosbak1.tgz"
bakupfile2="/macosbak/macosbak2.tgz"

if [ ! -d $bakupdevice ]; then
    echo "bakupfolder not exist,the bakupdevice is not ready,check it"
elif [ -d $bakupdevice -a -d $bakupfolder ]; then
    echo "bakupdevice is ok,bakupfolder exist"
    if [ -f $bakupfile1 -a -f $bakupfile2 ]; then
        echo "bakupfile1 exists,bakupfile2 exists"
        rm $bakupfile1
        mv $bakupfile2 $bakupfile1
        tar cvpzf $bakupfile2 --exclude=/macosbak --exclude=/Volumes --exclude="/Library/Application Support" --exclude=/Library/Caches --exclude=~/.cache --exclude=/private/var/log --exclude=~/.Trash --exclude="~/Documents/Virtual Machines.localized" --exclude=~/Downloads --exclude=~/Library/Caches --exclude=/private/var/tmp --exclude=/private/var/vm --exclude=/Users/Shared/Parallels /
    elif [ ! -f $bakupfile1 -a ! -f $bakupfile2 ]; then
        echo "bakupfile1 not exist,bakupfile2 not exist"
        tar cvpzf $bakupfile1 --exclude=/macosbak --exclude=/Volumes --exclude="/Library/Application Support" --exclude=/Library/Caches --exclude=~/.cache --exclude=/private/var/log --exclude=~/.Trash --exclude="~/Documents/Virtual Machines.localized" --exclude=~/Downloads --exclude=~/Library/Caches --exclude=/private/var/tmp --exclude=/private/var/vm --exclude=/Users/Shared/Parallels /
    elif [ -f $bakupfile1 -a ! -f $bakupfile2 ]; then
        echo "bakupfile1 exist,bakupfile2 not exist"
        tar cvpzf $bakupfile2 --exclude=/macosbak --exclude=/Volumes --exclude="/Library/Application Support" --exclude=/Library/Caches --exclude=~/.cache --exclude=/private/var/log --exclude=~/.Trash --exclude="~/Documents/Virtual Machines.localized" --exclude=~/Downloads --exclude=~/Library/Caches --exclude=/private/var/tmp --exclude=/private/var/vm --exclude=/Users/Shared/Parallels /
    elif [ ! -f $bakupfile1 -a -f $bakupfile2 ]; then
        echo "bakupfile1 not exist,bakupfile2 exist"
        mv $bakupfile2 $bakupfile1
        tar cvpzf $bakupfile2 --exclude=/macosbak --exclude=/Volumes --exclude="/Library/Application Support" --exclude=/Library/Caches --exclude=~/.cache --exclude=/private/var/log --exclude=~/.Trash --exclude="~/Documents/Virtual Machines.localized" --exclude=~/Downloads --exclude=~/Library/Caches --exclude=/private/var/tmp --exclude=/private/var/vm --exclude=/Users/Shared/Parallels /

    fi
elif [ -d $bakupdevice -a ! -d $bakupfolder ]; then
    echo "bakupdevice is ok,bakupfolder not exist"
    mkdir $bakupfolder
    tar cvpzf $bakupfile1 --exclude=/macosbak --exclude=/Volumes --exclude="/Library/Application Support" --exclude=/Library/Caches --exclude=~/.cache --exclude=/private/var/log --exclude=~/.Trash --exclude="~/Documents/Virtual Machines.localized" --exclude=~/Downloads --exclude=~/Library/Caches --exclude=/private/var/tmp --exclude=/private/var/vm --exclude=/Users/Shared/Parallels /
fi
