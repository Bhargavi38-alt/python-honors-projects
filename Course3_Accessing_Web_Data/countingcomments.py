import json
import urllib.request

url = input('Enter location: ').strip()
if len(url) < 1 : 
    print("enter url correctly")
    exit()

ans = urllib.request.urlopen(url)
data = ans.read().decode()
print('Retrieved',len(data),'characters')

info = json.loads(data)
com=info["comments"]
total=0
for i in com:
    total=total+int(i["count"])
print("total count=",total)
