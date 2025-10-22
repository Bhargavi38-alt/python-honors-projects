#program to obtain a nqqame in the 4th web page. so count is 4 position is 3? from web page
# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file
#this program goes to desired link's position in a url and scrapes data from that position and fetches it multiple times(count) which we can specify

#fetches or import desired package
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl



# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


#gather data
url = input('Enter the url- ')
cnt=input("Enter count-")
count=int(cnt)
position=input("enter position:")
pos=int(position)
#loop for desired number oftimes, integer cant be looped so use range

#first get the final page by looping and get href
for c in range(count): 
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    url= tags[pos-1].get('href')
 # now its a string, so split by _ and get last oe andsplit by . to remove html. save name in a variable and print variable

name=url.split('_')
last_name=name[-1]
final=last_name.split('.')
final_name=final[0]
print(final_name)


        
