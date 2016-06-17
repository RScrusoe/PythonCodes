import urlparse2
import html2text
from bs4 import BeautifulSoup
import urllib
import urllib.request
import re
import os
import csv
import re
import requests
search = input('Enter anything to download the related images  :  ')
n = int(input('Enter number of Images to download : '))
url = 'https://www.google.com/search?newwindow=1&safe=off&espv=2&biw=828&bih=667&tbm=isch&sa=1&q=' + search.replace(' ','+') +  '&oq=' + search.replace(' ','+')
#data = urllib.request.urlopen(url)


req = urllib.request.Request(
    url,
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)

f = urllib.request.urlopen(req)
#print(f.read().decode('utf-8'))
soup = BeautifulSoup(f,'html.parser')
ct = 0
for i in soup.findAll('a'):
    try:
        raw = str(i.get('href'))
        if 'imgurl' not in raw:
            continue
        tmp = raw.find('h')
        tmp2 = raw.find('&')
        img_url = raw[tmp:tmp2]
        name = img_url.split('/')[-1]
        urllib.request.urlretrieve(img_url,name)
        ct+=1
        print(str(ct) + ' Image Downloaded..')
    except:
        pass
    if ct ==n:
        break