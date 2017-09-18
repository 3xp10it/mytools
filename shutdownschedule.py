#!/usr/local/bin/python3
import os
from datetime import datetime
weekIndex = datetime.now().weekday()
if weekIndex not in [4,5, 6]:
    os.system("say cool boy,还有1分钟就要关机了")
    os.system("shutdown -h +1")
