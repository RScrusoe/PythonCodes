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
import time
import urllib
import requests

time1 = time.time()
def make_soup(url):
    req = urllib.request.Request(
    url,
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
    )
    data = urllib.request.urlopen(req)
    soup = BeautifulSoup(data,'html.parser')
    return soup
base_url = 'http://www.hdwallpapers.in'
url = 'http://www.hdwallpapers.in/celebrities-desktop-wallpapers/page/'
for z in range(2,225):
    if z == 21:
        continue
    print(z)
    url = url + str(z)
    soup = make_soup(url)
    list = []
    for i in soup.findAll('a',href=True):



        raw = base_url + i.get('href')
        if 'wallpapers.html' not in raw:
            continue
        if 'desktop' in raw:
            continue
        list.append(raw)
    for a in range (4):
        list.pop(0)
    #print(list)
    tlist = []
    for i in list:
        newsoup = make_soup(i)
        name = newsoup.find('h1').text + '.jpg'
        for j in newsoup.findAll('a',href=True):
            tmp = str(j.get('href'))
            if '.jpg' in tmp:
                tlist.append(str(base_url + tmp))
       # print(tlist)
        tlist.reverse()
        for k in tlist:

            if '3840x2160.jpg' in k:
                urllib.request.urlretrieve(k,name)
                print(k)
                break
            if '2560x1440.jpg' in k:
                urllib.request.urlretrieve(k,name)
                print(k)
                break
            if '1920x1080.jpg' in k:
                urllib.request.urlretrieve(k,name)
                print(k)
                break

