import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url processing
url = input('Enter location: ')
link = urllib.request.urlopen(url, context=ctx)
data = link.read()

#xml processing
tree = ET.fromstring(data)
counts = tree.findall('.//count')
count = 0
numbers = []

#To create a list with the texts in <count>
for digits in counts:
    numbers.append(int(digits.text))
    #counts the number of times the loop runs
    count += 1

print('Retrieving...', url)
print('Retrieved', len(data), 'characters')
print('Count: ', count)
print('Sum: ', sum(numbers))

#Sample data: http://py4e-data.dr-chuck.net/comments_42.xml
#Actual data: http://py4e-data.dr-chuck.net/comments_898399.xml