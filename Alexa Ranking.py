import html2text
from bs4 import BeautifulSoup
import urllib
import urllib.request
import re
import os
import csv
import re
import requests

site = input("Enter a website to check it's ALEXA ranking : ")
url='http://www.alexa.com/siteinfo/' + site
data = urllib.request.urlopen(url)
soup = BeautifulSoup(data,'html.parser')
t = soup.find('strong',{'class':'metrics-data align-vmiddle'})
print("Global Rank : " + str(t.text).lstrip())

t1 = soup.findAll('h4',{'class':'metrics-title'})
txt = soup.get_text().split('\n')
#print(txt)
i=0
for line in txt:
    if 'Rank in' in line:
        #print(line+': ',end='')
        #print(i)
        rank_in = line + ": "
        break
    i+=1
'''
#for string in soup.strings:
 #   print(repr(string.split('\n')))
new = []
j=0
for line in txt:
    j+=1
    if(j<=i):
        continue
    tmp = line
    tmp = str(tmp)
    tmp = tmp.lstrip()
    tmp = tmp.rstrip()
    tmp = tmp.replace(',','')
    if(tmp.isdigit()):
        new.append(tmp)
#print("##")
tmp1 = str(t.text).lstrip()
tmp1 = tmp1.replace(',','')
a = int(tmp1)
#print(len(new))
#print(new)
#print(a)
for k in range(100):
    if int(new[k]) < a:
        print(new[k])
        break
print('@@')
'''
A = True
for i in soup.findAll('strong',{'class':'metrics-data align-vmiddle'}):
    if A:
        A=False
        continue
    print(rank_in + (i.text).replace('\n',''))
    break