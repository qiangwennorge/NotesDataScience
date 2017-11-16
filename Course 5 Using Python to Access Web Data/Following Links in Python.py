import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')

if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
    #url = 'http://py4e-data.dr-chuck.net/known_by_Megan.html'

count = int(input('Enter count: '))
position = int(input('Enter position: '))

if count == None:
    count = 4
    #count = 7

if  position == None:
    position = 3
    #position = 18

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

print('Retrieving: ' + url)

#print(soup)

# Retrieve all of the anchor tags
tags = soup('a')

url_links = [tag.get('href', None) for tag in tags]

times = 0
while times < count:
    url_link = url_links[position - 1]
    print('Retrieving: ' + url_link)
    html = urllib.request.urlopen(url_link, context = ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    new_tags = soup('a') 
    url_links = [tag.get('href', None) for tag in new_tags]
    times += 1

target_name = re.findall(r'by_([A-Z][a-z]+).html', url_link)
print('The answer to the assignment is: ' + target_name[0])
