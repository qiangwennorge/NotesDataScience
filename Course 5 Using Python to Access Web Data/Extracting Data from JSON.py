import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter location: ')

if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_42.json'
    #url = 'http://py4e-data.dr-chuck.net/comments_49606.json'

uh = urllib.request.urlopen(url)

print('Retrieving', url)

data = uh.read().decode()
js = json.loads(data)

print('Retrieved', len(data), 'characters')

total_sum = 0
count = 0
for item in js['comments']:
    total_sum += int(item['count'])
    count += 1
    #print('Name', item['name'])
    #print('Id', item['id'])
    #print('Attribute', item['x'])

print('Count:',count)
print('Sum:',total_sum)
