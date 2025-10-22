import json
import urllib.request

url = input('Enter location: ')
if len(url) < 1 : 
    url='https://py4e-data.dr-chuck.net/comments_42.json'

ans = urllib.request.urlopen(url)
data = ans.read().decode()
print('Retrieved',len(data),'characters')

info = json.loads(data)
com=info["comments"]
total=0
for i in com:
    total=total+int(item["count"])
print("total count=",total)
