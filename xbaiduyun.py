import pdb
import platform
import argparse
import os
import sys
from exp10it import get_all_abs_path_file_name
if platform.system()=="Windows":
    print("not support windows")
    sys.exit(0)
parser = argparse.ArgumentParser(
    description="")
parser.add_argument(
    "-d", help="The directory contains files")
parser.add_argument(
    "-o", help="The output directory")
args = parser.parse_args()
source_dir= args.d
output_dir=args.o
if output_dir is None:
    print("未指定输出文件夹")
    print("eg: python3 %s -d inputdir -o outputdir" % __file__)
    sys.exit(0)
if source_dir is None:
    print("未指定输入文件夹")
    print("eg: python3 %s -d inputdir -o outputdir" % __file__)
    sys.exit(0)
if not os.path.exists(source_dir):
    print("输入文件夹路径不存在,请指定一个存在的文件夹并重新运行")
    print("eg: python3 %s -d inputdir -o outputdir" % __file__)
    sys.exit(0)
if os.path.exists(output_dir):
    print("输出文件夹已存在,请指定一个当前不存在的新的输出文件夹并重新运行")
    print("eg: python3 %s -d inputdir -o outputdir" % __file__)
    sys.exit(0)
os.mkdir(output_dir)
filelist=get_all_abs_path_file_name(source_dir,[])
for abs_file_path in filelist:
    source_file_abs_path=abs_file_path
    filename=source_file_abs_path.split("/")[-1]
    output_file_abs_path=output_dir+"/"+filename
    cmd='''cp "%s" "%s" && echo niaho >> "%s"''' % (source_file_abs_path,output_file_abs_path,output_file_abs_path)
    os.system(cmd)
print("finished:)")
