from rohan import *

url = 'http://dl2.my98music.com/Data/Serial/Gotham/S02/'
l = []
soup = make_soup(url)
print('@@')
for i in soup.findAll('a'):
    if '480' in str(i['href']):
        l.append(url + i['href'])

for i in l:
    print(i)


    