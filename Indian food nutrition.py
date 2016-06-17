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
outfile = open('Indian Food Nutrition.csv','wb')
header = 'Food, Serving Size, Calories, Fat, Carbohydrates, Protein'+'\n'
outfile.write(bytes(header,encoding="ascii", errors='ignore'))

for i in range(1,5):
    #print(i)
    url='http://www.myfitnesspal.com/nutrition-facts-calories/indian-food/'+ str(i)
    data = urllib.request.urlopen(url)
    soup = BeautifulSoup(data,'html.parser')
    for j in soup.findAll('div',{'class':'food_info'}):
        #print(j.text)
        data2 = j.text.split('\n')
        list = []
        for i in data2:
            i = str(i)
            i = i.replace('\t','')
            if i != '':
                list.append(i)
        #print(list)
        tmp = list.pop(0)
        list[0] = str(tmp + list[0]).replace(',','')
        list[1] = str(list[1]).replace(',','')[13:]
        list[2] = str(list[2]).replace(',','')[11:]
        list[3] = str(list[3]).replace(',','')[6:]
        list[4] = str(list[4]).replace(',','')[8:]
        list[5] = str(list[5]).replace(',','')[10:]

        #print(list)


        rowdata = ''
        for i in list:
            rowdata = rowdata + str(i) + ' , '
        rowdata = rowdata + '\n'
        #print(rowdata)
        outfile.write(bytes(rowdata,encoding="ascii", errors='ignore'))