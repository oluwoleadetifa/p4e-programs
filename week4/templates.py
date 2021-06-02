import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url- ')
count = int(input('Enter count- '))
position = int(input('Enter position- '))

for i in range(count+1):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    print('Retrieving: ', url)
    # Retrieve all of the anchor tags
    tags = soup.findAll('a')
    tag = tags[position-1]
    link = tag.get('href', None)
    
    url = link


# sample data  http://py4e-data.dr-chuck.net/known_by_Fikret.html
# actual data http://py4e-data.dr-chuck.net/known_by_Shannyn.html