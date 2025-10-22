#program to calculate by taking values from web page
# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
total = 0
spans = soup.find_all("span")

for sp in spans:
    text = sp.get_text(strip=True)  # extract inner text
    if text.isdigit():              # check if it's a number
        total += int(text)
print(total)
# Retrieve all of the anchor tags
#tags = soup('a')
#for tag in tags:
    #print('TAG:', tag)
    #print('URL:', tag.get('href', None))
    #print('Contents:', tag.contents[0])
    #print('Attrs:', tag.attrs)
    
   