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
#macos系统备份脚本，备份产生一个文件,macosbak1.tgz为上一次备份的文件
# crontab -e like：
# m h  dom mon dow   command
#18  8    5 * *   root    bash /usr/share/mytools/macosbak.sh

bakupdevice="/"
bakupfolder="/macosbak/"
bakupfile1="/macosbak/macosbak1.tgz"

if [ ! -d $bakupdevice ]; then
    echo "bakupfolder not exist,the bakupdevice is not ready,check it"
elif [ -d $bakupdevice -a -d $bakupfolder ]; then
    echo "bakupdevice is ok,bakupfolder exist"
    if [ -f $bakupfile1 ]; then
        rm $bakupfile1
        tar cvpzf $bakupfile1 --exclude=/macosbak --exclude=/Volumes --exclude="/Library/Application Support" --exclude=/Library/Caches --exclude=~/.cache --exclude=/private/var/log --exclude=~/.Trash --exclude="~/Documents/Virtual Machines.localized" --exclude=~/Downloads --exclude=~/Library/Caches --exclude=/private/var/tmp --exclude=/private/var/vm /
    fi
elif [ -d $bakupdevice -a ! -d $bakupfolder ]; then
    echo "bakupdevice is ok,bakupfolder not exist"
    mkdir $bakupfolder
    tar cvpzf $bakupfile1 --exclude=/macosbak --exclude=/Volumes --exclude="/Library/Application Support" --exclude=/Library/Caches --exclude=~/.cache --exclude=/private/var/log --exclude=~/.Trash --exclude="~/Documents/Virtual Machines.localized" --exclude=~/Downloads --exclude=~/Library/Caches --exclude=/private/var/tmp --exclude=/private/var/vm /
fi
