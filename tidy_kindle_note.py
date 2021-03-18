import pdb
import os
import re
with open("/tmp/1","r+") as f:
    lines_to_tidy=f.readlines()
_lines_to_tidy=[]
for line in lines_to_tidy:
    if re.match(r"^\s+$",line):
        pass
    else:
        if len(line)<5:
            pass
        else:
            _lines_to_tidy.append(line)

def tidy_all_lines(lines):
    if len(lines) in [0,1]:
        return lines
    else:
        _1=lines[0]
        _2=tidy_all_lines(lines[1:])
        #pdb.set_trace()
        if _1[int(len(_1)*0.25):-int(len(_1)*0.25)] in _2[0]:
            if len(_1)>len(_2[0]):
                return [_1]+_2[1:]
            else:
                return _2
        else:
            return [_1]+_2

new_lines=tidy_all_lines(_lines_to_tidy)
with open("/tmp/2","a+") as f:
    for line in new_lines:
        f.write("- "+line+"\n")


