import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter location: ')
web = urllib.request.urlopen(url).read().decode()
print('Retrieving', url)
print('Retrieved', len(web), 'characters')


#data calculation
count = 0
total = 0
tree = ET.fromstring(web)
tags = tree.findall('.//count')
for tag in tags:
    count += 1
    total += int(tag.text)

print('Count:', count)
print('Sum:', total)