import os
import platform
config = os.path.expanduser("~") + "/.password"
with open(config, "r+") as f:
    _ = eval(f.read())
filename = _['file']
password = _['pass']
os.system("openssl aes-256-cbc -d -in %s -out ~/.password_tmp_file -k '%s'" %
          (filename, password))
system=platform.system()
if system=="Darwin":
    cmd="/Applications/MacVim.app/Contents/MacOS/Vim ~/.password_tmp_file"
else:
    cmd="vim  ~/.password_tmp_file"
os.system(cmd)
os.system("openssl aes-256-cbc -in ~/.password_tmp_file -out %s -k '%s'" %
          (filename, password))
os.system("rm ~/.password_tmp_file")
