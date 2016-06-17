import urllib
import urllib.request
from bs4 import BeautifulSoup
url = "http://www.hdwallpapers.in/search.html?q=shraddha"
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
i=1
for img in soup.findAll('img'):
    tmp = img.get('src')
    if tmp[:1] == '/':
        image = 'http://www.hdwallpapers.in/search.html?q=shraddha' + tmp
    else :
        image = tmp
    nametmp = img.get('alt')
    if len(nametmp)==0:
        filename = str(i)
        i+=1
    else:
        filename=nametmp
    imagefile = open(filename + '.jpg','wb')
    imagefile.write(urllib.request.urlopen(image).read())
    imagefile.close()
    print(tmp)