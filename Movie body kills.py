from html2text import html2text
from bs4 import BeautifulSoup
import urllib
import urllib.request
import re
import os
file = open(os.path.expanduser("Movie_Kills.csv"),'wb')
header = 'Movie Title, On Screen Kills'
file.write(bytes(header,encoding="ascii", errors='ignore'))

for i in range(65,91):
    if i == 81:
        continue
    if i ==86:
        i=118
    if i == 88:
        i = 120
    urltmp = 'http://www.moviebodycounts.com/movies-'+chr(i)+'.htm'
    page = urllib.request.urlopen(urltmp)
    soup = BeautifulSoup(page, 'html.parser')
    for links in soup.findAll('a'):
        if links.get('href')[:1]==chr(i):
            movie_page_link = 'http://moviebodycounts.com/' + str(links.get('href'))

            print(movie_page_link)
            movie_page = urllib.request.urlopen(movie_page_link)
            newsoup = BeautifulSoup(movie_page,'html.parser')
            t = re.compile('Film')
            t1 = newsoup.findAll(text=t)
            if t1 == []:
                t = re.compile('Kills')
                t1 = newsoup.findAll(text=t)
            if t1 == []:
                continue
            t2 = str(t1[0]).split('\n')
            l=[]
            flag = 0
            for a in t2:
                #print(a)
                l.append(str(a).split(' '))
            #print(l)
            for a in l:
                if flag == 1:
                    break
                #if str(a).isdigit():
                for b in a:
                    if str(b).isdigit():
                        tmpname = str(links.get('href'))[:-4]
                        rowdata = tmpname + ',' + b
                        rowdata+= '\n'
                        print(rowdata)
                        file.write(bytes(rowdata,encoding="ascii", errors='ignore'))
                        #writer.writerow(['Spam'] * 5 + ['Baked Beans'])
                        #writer.writerow(('sdfsdfsdf','52211'))
                        flag=1
                        break

