from rohan import *

url = 'http://dl2.my98music.com/Data/Serial/Better%20Call%20Saul/Season%202/'
l = []
soup = make_soup(url)
print('@@')
for i in soup.findAll('a'):
    if '480' in str(i['href']):
        l.append(url + i['href'])

for i in l:
    print(i)


    