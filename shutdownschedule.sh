xinqi=`date | ack '星期\S+' -o`
if [ "$xinqi" != "星期六" -a "$xinqi" != "星期天" ]; then
    say 主人主人,还有1分钟就要关机了
    shutdown -h +1
fi
