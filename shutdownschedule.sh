xinqi=`date | ack '星期\S+' -o`
if [ "$xinqi" != "星期六" -a "$xinqi" != "星期天" ]; then
    shutdown -h +1
fi
