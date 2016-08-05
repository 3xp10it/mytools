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
### name: ubuntubak.sh
### function: bakup system
### date: 2016-08-05
### author: quanyechavshuo
### blog: https://3xp10it.github.io
#############################################################
#系统备份脚本，备份产生两个文件,ubuntubak2.tgz为最新备份文件,ubuntubak1.tgz为上一次备份的文件
# crontab -e like：
# m h  dom mon dow   command
#18  8    5 * *   root    bash /usr/share/mytools/ubuntubak.sh

bakupdevice="/media/root/files"
bakupfolder="/media/root/files/ubuntubak/"
bakupfile1="/media/root/files/ubuntubak/ubuntubak1.tgz"
bakupfile2="/media/root/files/ubuntubak/ubuntubak2.tgz"
if [ ! -d $bakupdevice ]; then
    echo "bakupfolder not exist,the bakupdevice is not ready,check it"
elif [ -d $bakupdevice -a -d $bakupfolder ]; then
    echo "bakupdevice is ok,bakupfolder exist"
    if [ -f $bakupfile1 -a -f $bakupfile2 ]; then
        echo "bakupfile1 exists,bakupfile2 exists"
        rm $bakupfile1
        mv $bakupfile2 $bakupfile1
        tar cvpzf $bakupfile2 --exclude=/proc --exclude=/lost+found --exclude=/ubuntubak.tgz --exclude=/mnt --exclude=/sys --exclude=/media --exclude=/root/.cache /
    elif [ ! -f $bakupfile1 -a ! -f $bakupfile2 ]; then
        echo "bakupfile1 not exist,bakupfile2 not exist"
        tar cvpzf $bakupfile1 --exclude=/proc --exclude=/lost+found --exclude=/ubuntubak.tgz --exclude=/mnt --exclude=/sys --exclude=/media --exclude=/root/.cache /
    elif [ -f $bakupfile1 -a ! -f $bakupfile2 ]; then
        echo "bakupfile1 exist,bakupfile2 not exist"
        tar cvpzf $bakupfile2 --exclude=/proc --exclude=/lost+found --exclude=/ubuntubak.tgz --exclude=/mnt --exclude=/sys --exclude=/media --exclude=/root/.cache /
    elif [ ! -f $bakupfile1 -a -f $bakupfile2 ]; then
        echo "bakupfile1 not exist,bakupfile2 exist"
        mv $bakupfile2 $bakupfile1
        tar cvpzf $bakupfile2 --exclude=/proc --exclude=/lost+found --exclude=/ubuntubak.tgz --exclude=/mnt --exclude=/sys --exclude=/media --exclude=/root/.cache /

    fi
elif [ -d $bakupdevice -a ! -d $bakupfolder ]; then
    echo "bakupdevice is ok,bakupfolder not exist"
    mkdir $bakupfolder
    tar cvpzf $bakupfile1 --exclude=/proc --exclude=/lost+found --exclude=/ubuntubak.tgz --exclude=/mnt --exclude=/sys --exclude=/media --exclude=/root/.cache /
fi
