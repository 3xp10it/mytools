# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#必须加上上面四行,否则各种编码的错误爆出

import os
import datetime

date=datetime.date.today()
print "please input blog article title:)"
title=raw_input()
print "please input blog categories:)"
categories=raw_input()
print "please input blog tags,use space to separate:)"
tags=raw_input()
tags_list=tags.split(' ')
tags_write_to_file=""
for each in tags_list:
    tags_write_to_file+=(' - '+each+'\\\n')
tags_write_to_file=tags_write_to_file[:-2]


article_title=title
title1=title.replace(' ','-')
filename=str(date)+'-'+title1+'.md'

file_abs_path="/root/myblog/_posts/"+filename
os.system("cp /root/myblog/_posts/*webshell* %s" % file_abs_path)
os.system("sed -i 's/^title.*/title:      %s/g' %s" % (title,file_abs_path))
os.system("sed -i 's/date:       .*/date:       %s/g' %s" % (str(date),file_abs_path))
os.system("sed -i 's/summary:    隐藏webshell的几条建议/summary:    %s/g' %s" % (title,file_abs_path))
os.system("sed -i '11,$d' %s" % file_abs_path)
os.system("sed -i 's/categories: webshell/categories: %s/g' %s" % (categories,file_abs_path))
os.system("sed '/ - webshell/c\\\n%s' %s > /tmp/1" % (tags_write_to_file,file_abs_path))
os.system("cat /tmp/1 > %s && rm /tmp/1" % file_abs_path)
os.system("vim %s" % file_abs_path)

print "do you want to update your remote 3xp10it.github.io's blog?"
print "your chioce: Y/n,default[Y]:>",
upa=raw_input()
if(upa=='n' or upa=='N'):
    print 'done!bye:D'
else:
    succeed=os.system("bash /usr/share/mytools/up.sh")
    if(succeed==0):
        os.system("firefox %s" % "https://3xp10it.github.io")

