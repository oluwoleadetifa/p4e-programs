import urllib.request, urllib.parse, urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter Location: ')
link = urllib.request.urlopen(url, context=ctx)
data = link.read()

info = json.loads(data)
numbers = []
count = 0

for digits in info['comments']:
    numbers.append(int(digits['count']))
    count += 1

print('Retrieving...', url)
print('Retrieved', len(data), 'characters')
print('Count: ', count)
print('Sum: ', sum(numbers))



# http://py4e-data.dr-chuck.net/comments_42.json
# http://py4e-data.dr-chuck.net/comments_898400.json
