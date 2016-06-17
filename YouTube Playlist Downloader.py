
from bs4 import BeautifulSoup
import urllib
import urllib.request


import time
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


url = str(input("Enter URl of YouTube playlist to download complete playlist : "))
soup = make_soup(url)
data = soup.find('div',{'class':'j'})
ct=1
list = []
for i in soup.findAll('a',href=True):
    if 'watch' in str(i['href']):
        video_url = 'https://www.youtube.com'+str(i['href'])

        tmp = video_url.find('&')
        video_url = video_url[:tmp]
        tmp1=video_url.find('=')+1
        video_url = video_url[tmp1:]
        ct+=1
        if video_url not in list:
            list.append(video_url)
Name=''
def pass_name(name):
    Name=name
    return Name

ct=1

for i in list:
    try:
        print (ct)
        new_list=[]
        url = 'http://keepvid.com/?url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D'+i
        soup = make_soup(url)
        tmp=str(soup.find('div',{'id':'info'}).text)
        tmp1=tmp.find('youtube.com')
        name=str(tmp[:tmp1])+'.mp4'
        for j in soup.findAll('a',{'class':'l'}):
            new_list.append(j['href'])
        pass_name(name)
        print('Downloading '+name )
        #name = str(ct) + '.mp4'
        urllib.request.urlretrieve(new_list[1],name)   #new_list[1] that 1 for selecting 720p
        ct+=1
        pass_name(new_list[1])


    except FileNotFoundError:
        name = str(ct) + '.mp4'
        #print(Name)
        urllib.request.urlretrieve(Name,name)   #new_list[1] that 1 for selecting 720p
        ct+=1
    except:
        print("Couldn't Download this video")

time2=time.time()
print('\nTotal Download Time = ' + str((time2-time1)/60)+ ' min')