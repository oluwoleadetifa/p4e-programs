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
number = 0 
counter = 0

for i in range(count+1):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    print('Retrieving: ', url)
    # Retrieve all of the anchor tags
    tags = soup.findAll('a')
    for tag in tags:
        # to pick only the third link in the website
        if number != position:
            link = tag.get('href', None)
            number += 1
        else:
            linked = link
            number = 0

    url = linked


# sample data  http://py4e-data.dr-chuck.net/known_by_Fikret.html
# actual data http://py4e-data.dr-chuck.net/known_by_Shannyn.html