import urllib
import re
import requests
symbols  = ["aapl", "goog", "ba", "nflx", "ge", "ttm", "bhel.ns", "wmt"]
i=0



while i < len(symbols):
    url = "http://finance.yahoo.com/q?s="+ symbols[i]
    regex = '<span id="yfs_l84_' +symbols[i]+'">(.+?)</span>'
    pattern = re.compile(regex)
    htmlfile = requests.get(url)
    htmltext = htmlfile.text
    price = re.findall(pattern, htmltext)
    print("price of ", symbols[i], "is ", price)
    i+=1


'''

#http://www.bloomberg.com/markets/chart/data/1D/AAPL:US

import urllib
import re
import requests
import csv

symbols = []
csvfile = csv.reader(open("companylist.csv", "r"))
for row in csvfile:

    symbols.append(((row[0]).lower()))

i = 0

while i < len(symbols):
    url = "http://finance.yahoo.com/q?s=" + symbols[i]
    regex = '<span id="yfs_l84_' + symbols[i] + '">(.+?)</span>'
    pattern = re.compile(regex)
    htmlfile = requests.get(url)
    htmltext = htmlfile.text
    price = re.findall(pattern, htmltext)
    print("price of ", symbols[i], "is ", price)
    i += 1

'''



## with multi threading:::: :::::::::::::::::::::::::::::::::



'''

import urllib
import re
import requests
import csv
from threading import Thread

symbols = []
csvfile = csv.reader(open("companylist.csv", "r"))
for row in csvfile:

    symbols.append(((row[0]).lower()))


def th(ur):
    base = "http://finance.yahoo.com/q?s=" + ur


    i = 0



    regex = '<span id="yfs_l84_' + ur + '">(.+?)</span>'
    pattern = re.compile(regex)
    htmlfile = requests.get(base)
    htmltext = htmlfile.text
    price = re.findall(pattern, htmltext)
    print("price of ", ur , "is ", price)
    i += 1

threadlist = []
for u in symbols:
    t = Thread(target=th,args=(u,))
    t.start()
    threadlist.append(t)

for b in threadlist:
    b.join()


'''

#using web srawler re.search
'''
import re
import requests
import csv

symbols = []
csvfile = csv.reader(open("companylist.csv", "r"))
for row in csvfile:

    symbols.append(((row[0]).lower()))
symbols.pop(0)

for symb in symbols:

   url = "http://www.google.com/finance?q="

   url2 = url+symb
   data = requests.get(url2).text
   m = re.search('span class="pr"', data)
   if(m==None):
       continue
   start = m.end()
   end = start+50
   data1 = data[start:end]
   m= re.search(('">'),data1)
   start = m.end()
   data2 = data1[start:(start+14)]
   m = re.search('/',data2)
   new_end=(m.start())-1
   print(data2[:new_end])


'''