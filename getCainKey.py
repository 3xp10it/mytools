#参数为文件名
#也即cain目录下的.lst文件[pop3.lst,http.lst,smtp.lst,imap.lst,ftp.lst,...等包含用户名口令的文件]
#效果为在程序当前目录下生成一个xxx-cain_out_put.txt为整理后的文件
import re
import sys
with open(sys.argv[1],"r+") as f:
    all_lines=f.readlines()
AddedLines=[]
for each_line in all_lines:    
    #a=re.search(r"[\S]+\s+-\s+[\S]+\s+[\S]+\s+[\S]+\s+([\S]+)\s+([\S]+)\s+[\S]+\s",each_line,re.I)
    a=re.search(r"[\S]+\s+-\s+[\S]+\s+[\S]+\s+[\S]+\s+([\S]+)\s+([\S]+).*\s",each_line,re.I)
    if a:
        user_field=a.group(1)
        pass_field=a.group(2)
        string2write=user_field+":"+pass_field+"\n"
        print(string2write)
        if string2write not in AddedLines:
            should_write=1
            for each in AddedLines:
                if each[:len(user_field)]!=user_field: 
                    continue
                else:
                    if pass_field==each.split(":")[1][:-1]:
                        should_write=0
                    break
            if should_write==1:
                AddedLines.append(string2write)
                with open(sys.argv[1]+"-cain_out_put.txt","a+") as f:
                    f.write(string2write)
