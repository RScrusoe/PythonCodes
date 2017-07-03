from rohan import *
from multiprocessing.dummy import Pool as ThreadPool 

l=[]
ul=[]


def factslide(x):
	
	soup = make_soup('http://www.factslides.com' + str(x))

	for i in soup.findAll('div',{'class':'i'}):
		aa = str(i.text).strip().replace('\n',' ')
		if not(aa == '' or aa =='\n'):
			l.append(aa) 


def prep_list():
	url = 'http://www.factslides.com/s-Pluto'
	soup = make_soup(url)

	for i in soup.findAll('div',{'id':'slideshows_menu_left'}):
		for j in i.findAll('div'):
			for x in j.findAll('a'):
				ul.append(x['href'])
				
prep_list()

with ThreadPool(20) as pool:
    results = pool.map(factslide, ul)


for i,j in enumerate(l):
	print(i+1,end='-->')
	print(j)
