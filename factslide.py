from rohan import *
from multiprocessing.dummy import Pool as ThreadPool 

l=[]
ul=[]
ind = [i for i in range(1,1001)]


def factslide(x):
	
	soup = make_soup('http://www.factslides.com' + str(x))

	for i in soup.findAll('li',{'itemprop':'itemListElement'}):
		l.append(i.text)


# for i in range(1,6):
# 	factslide(i)

# for i,j in enumerate(l):
# 	print(i,end='-->')
# 	print(j)

def prep_list():
	url = 'http://www.factslides.com/s-Indonesia'
	soup = make_soup(url)

	for i in soup.findAll('div',{'id':'slideshows_menu_left'}):
		for j in i.findAll('div'):
			for x in j.findAll('a'):
				ul.append(x['href'])
				
prep_list()



with ThreadPool(20) as pool:
    results = pool.map(factslide, ul)


for i,j in enumerate(l):
	print(i+9444,end='-->')
	print(j)
