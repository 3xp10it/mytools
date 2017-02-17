#参数为文件名
#也即cain目录下的.lst文件[pop3.lst,http.lst,smtp.lst,imap.lst,ftp.lst,...等包含用户名口令的文件]
#效果为在程序当前目录下生成一个xxx-cainOutPut.txt为整理后的文件
import re
import sys
with open(sys.argv[1],"r+") as f:
    allLines=f.readlines()
AddedLines=[]
for eachLine in allLines:    
    #a=re.search(r"[\S]+\s+-\s+[\S]+\s+[\S]+\s+[\S]+\s+([\S]+)\s+([\S]+)\s+[\S]+\s",eachLine,re.I)
    a=re.search(r"[\S]+\s+-\s+[\S]+\s+[\S]+\s+[\S]+\s+([\S]+)\s+([\S]+).*\s",eachLine,re.I)
    if a:
        userField=a.group(1)
        passField=a.group(2)
        string2write=userField+":"+passField+"\n"
        print(string2write)
        if string2write not in AddedLines:
            shouldWrite=1
            for each in AddedLines:
                if each[:len(userField)]!=userField: 
                    continue
                else:
                    if passField==each.split(":")[1][:-1]:
                        shouldWrite=0
                    break
            if shouldWrite==1:
                AddedLines.append(string2write)
                with open(sys.argv[1]+"-cainOutPut.txt","a+") as f:
                    f.write(string2write)
