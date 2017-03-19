import requests
import re
html=requests.get("https://github.com/macvim-dev/macvim/releases/").text
a=re.findall(r'''href="(.*\.dmg)"''',html,re.I)
macvimUrl="https://github.com"+a[0]
print(macvimUrl)

