import pdb
import os
import time
import re
import requests
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
while True:
    html = get_string_from_command("phantomjs /tmp/xstock.js")
    find_price = re.search(r'''01318aprice[^\d\.]+([\d\.]+)''', html)
    find_change = re.search(r'''01318achange[^\d\.]+([\d\.]+)''', html)
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
    output.good_print(price+"    "+change,color)
    time.sleep(1)
