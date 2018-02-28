from __future__ import print_function
from drawille import Canvas
import pdb
import os
import time
import re
from collections import deque
from exp10it import get_string_from_command
from exp10it import CLIOutput
output = CLIOutput()
phantom_js = '''
var webPage = require('webpage');
var page = webPage.create();

page.open('http://so.hexun.com/default.do?type=stock&key=601318', function(status) {
  console.log('Status: ' + status);
  console.log(page.content);
  phantomjs.exit();
});
'''
if not os.path.exists("/tmp/xstock.js"):
    with open("/tmp/xstock.js", "a+") as f:
        f.write(phantom_js)
x = 0
price_list = deque([])
while True:
    html = get_string_from_command("phantomjs /tmp/xstock.js")
    find_price = re.search(r'''01318aprice[^\d\.]+([\d\.]+)''', html)
    find_change = re.search(r'''01318achange.+>([^<>\s]+)<''', html)
    price = "null"
    change = "null"
    color = "green"
    if find_change:
        change = find_change.group(1)
        if "-" not in change:
            color = "red"
    else:
        print("0ps,can't find change")
    if find_price:
        price = find_price.group(1)
    else:
        print("0ps,can't find price")
    curtime = time.strftime('%H:%M:%S', time.localtime(time.time()))
    output.good_print(curtime + "    " + price + "    " + change, color)
    if float(price) >= 75:
        input("Attention,>75")
    if float(price) > 80:
        input("Attention,>80")
    # show 200 count=3minutes--4minutes
    if x / 10 > 200:
        price_list.append(price)
        price_list.popleft()
    else:
        price_list.append(price)
    x += 10
    c = Canvas()
    for i in range(0, 3600):
        c.set(i, (10 * float(price_list[i]) - 700) * 10)
        if len(price_list) < 3600 and i == len(price_list) - 1:
            break
    output.good_print(c.frame(), color)
    time.sleep(1)
