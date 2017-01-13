#import urlparse2
#import html2text
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
import random
#from tkinter import *
#import pdfcrowd



from random import choice



time1 = time.time()
user_agents = [
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9'
]



def make_soup(url):
    req = urllib.request.Request(
    url,
    data=None,
    headers={
        'User-Agent': choice(user_agents)
    }
    )
    data = urllib.request.urlopen(req)
    soup = BeautifulSoup(data,'html.parser')
    return soup
'''
print("asdasdasd")
url = 'https://twitter.com/GoogleFacts'
soup = make_soup(url)
#f = open('test.htm','w')
#f.write(soup.prettify())
#print('done!')
for a in soup.findAll('p',{'class':'TweetTextSize TweetTextSize--26px js-tweet-text tweet-text'}):
    print("##  ",end='')
    print(a.get_text())
print('done!')
'''


next_url = 'https://en.wikipedia.org/wiki/Physics'

heading = []

while len(heading) < 25:
    soup = make_soup(next_url)
    for p in soup.findAll('div', {'id':'mw-content-text'}):
        #print(p)
        for a in p.findAll('span'):
            x = a.find('a')
            if x != None:
                
                
                next_heading = x.get_text()
                heading.append(next_heading)
                print(next_heading,next_url)
                next_url = 'https://en.wikipedia.org' + x['href']

                break
