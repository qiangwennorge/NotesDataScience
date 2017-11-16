import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter URL: ')

if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_42.xml'

data = urllib.request.urlopen(url).read()

tree = ET.fromstring(data)

lst = tree.findall('.//count')

total_sum = 0

for item in lst:
    total_sum += int(item.text)
    #print('Count: ', item.text)

print('The sum is: ', total_sum)
