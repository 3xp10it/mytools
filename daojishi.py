import os
import time
import sys
since = time.time()
while True:
    time.sleep(1)
    time_elapsed = time.time() - since
    used_time=('{:.0f}: {:.0f}'.format(time_elapsed // 60, time_elapsed % 60))
    cmd="figlet -c -f basic %s" % used_time
    os.system(cmd)
