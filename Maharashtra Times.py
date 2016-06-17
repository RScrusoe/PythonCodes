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
print("Maharashtra Times\n")
url = 'http://maharashtratimes.indiatimes.com'
data = urllib.request.urlopen(url)
soup = BeautifulSoup(data,'html.parser')
ct =1   #Count of MT news article
for i in soup.findAll('a',href=True):
    i=str(i.get('href'))
    if 'horoscope' in i:
        continue
    if '.cms' and 'articleshow' in i:
        if 'maharashtratimes' in i:
            pass
            #print(i)
        else:
            i= 'http://maharashtratimes.indiatimes.com' + i
            #print(i)
        article_url = i
        #print(i)
        article_data = urllib.request.urlopen(article_url)
        newsoup = BeautifulSoup(article_data,'html.parser')
        #print(newsoup.find('div',{'class':'Normal'}))
        for a in  newsoup.findAll('div',{'class':'Normal'}):

            print('\n'+ str(ct))
            print(newsoup.find('h1').text)
            print(a.text)
    ct+=1