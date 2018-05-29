# 运行方法
# c:\python34\python setup.py py2exe
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
