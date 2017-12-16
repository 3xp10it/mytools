#!/usr/local/bin/python3
import os
from datetime import datetime
week_index = datetime.now().weekday()
if week_index not in [4,5, 6]:
    os.system("say cool boy,还有2分钟就要关机了")
    os.system("shutdown -h +2")
