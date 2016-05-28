#rime文本字典去重精简脚本
import sys
fp=open(sys.argv[1])
all=fp.readlines()
fp.close()
#print len(all)
newall2in3=[]
fp=open("newdic.txt","a+")
for eachline in all:
    if "#" not in eachline:
        eachline2in3=eachline.split('\t')[:2]
        if eachline2in3 not in newall2in3 and 'enc' not in eachline and ' ' not in eachline2in3[0] and (eachline2in3[0][0]<'a' or eachline2in3[0][0]>'z'):
            newall2in3.append(eachline2in3)
            fp.write(eachline)

#print len(newall)
fp.close()

