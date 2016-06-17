
base_url = 'http://www.lonny.com/Celebrity+Homes/articles/3qY78bVuhwP/Taylor+Swift+Beverly+Hills+CA'
soup = make_soup(base_url)


def d(url):
    newsoup = make_soup(url)
    s = newsoup.find('img',{'id':'currentPic'})
    img_url = s['src']
    n = newsoup.find('div',{'id':'specialBoxTitle'})
    nm = str(n.get_text())
    st = nm.find('.')
    stp = nm.find(')')
    print(st)
    print(stp)
    name = nm[(st+1):(stp+1)] + '.jpg'


    urllib.request.urlretrieve(img_url,name)


def details(url):
    nsoup = make_soup(url)
    s=nsoup.find('div',{'id':'specialBoxBody'})
    det = s.get_text()
    print(det)
for i in soup.findAll('a',{'class':'_c btn-theme btn-next'}):
    try:
        u = i['href']
        print(u)
        d(u)
        details(u)


    except:
        print("failed")
        continue