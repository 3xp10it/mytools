import re
import pdb
import base64
with open("burphistory","r+") as f:
    all=f.read()
g=re.findall(r"<request base64=.*>.*</request>\s+<status>\d+</status>\s+<responselength>\d+</responselength>\s+<mimetype>\w+</mimetype>\s+<response base64=.*>.*</response>",all)
out_list=[]
for each in g:
    groups=re.search(r"<request base64=.*?><!\[CDATA\[(.*)\]\]></request>\s+<status>(\d+)</status>\s+[\s\S]*?<response base64=.*?><!\[CDATA\[(.*)\]\]></response>",each)
    request=groups.group(1)
    status=groups.group(2)
    response=groups.group(3)

    _request=request.encode(encoding="utf-8")
    request=base64.b64decode(_request)
    request=request.decode("utf8","ignore")

    _response=response.encode(encoding="utf-8")
    response=base64.b64decode(_response)
    response=response.decode("utf8","ignore")

    if "127\.0\.0\.1" in request:
        with open("output1.txt","a+") as f:
            f.write(request+"\r\n"+"status="+str(status)+"\r\n"+response)
