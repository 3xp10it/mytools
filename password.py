import os
config = os.path.expanduser("~") + "/.password"
with open(config, "r+") as f:
    _ = eval(f.read())
filename = _['file']
password = _['pass']
os.system("openssl aes-256-cbc -d -in %s -out ~/.password_tmp_file -k '%s'" %
          (filename, password))
os.system("/Applications/MacVim.app/Contents/MacOS/Vim ~/.password_tmp_file")
os.system("openssl aes-256-cbc -in ~/.password_tmp_file -out %s -k '%s'" %
          (filename, password))
os.system("rm ~/.password_tmp_file")
