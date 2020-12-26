import urllib.request, urllib.parse, urllib.error
import json

link = input('Enter location: ')
print('Retrieving', link)
html = urllib.request.urlopen(link).read().decode()
print('Retrieved', len(html), 'characters')

try:
    js = json.loads(html)
except:
    js = None

count = 0
total = 0

for line in js['comments']:
    total += int(line['count'])
    count += 1

print('Count:', count)
print('Sum:', total)