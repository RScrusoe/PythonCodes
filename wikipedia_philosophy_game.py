#import urlparse2
#import html2text
from bs4 import BeautifulSoup
import urllib
import urllib.request
import requests

#If you open any wikipedia article, and start clicking on the first link, you will end up on Philosophy article.
#This program proves it


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



next_url = 'https://en.wikipedia.org/wiki/Prison'

heading = []

for x in range(50):

    soup = make_soup(next_url)

    for i in soup.findAll('p'):
        if '<a' not in str(i):
            continue
        elif ('<td' == str(i.parent)[:3]):
            continue
        else:
            
            for j in i.findAll('a'):
                if ('commons' in str(j)) or ('File' in str(j)) or ('Help' in str(j)) or ('Media' in str(j)) or ('cite' in str(j)) or ('Ancient_Greek' in str(j)) or ('wiktionary' in str(j)) : 
                    continue

                else:
                    print(j.text)
                    next_url = 'https://en.wikipedia.org' + j['href']
                    break
            break
    if 'Philosophy' in next_url:
        break
