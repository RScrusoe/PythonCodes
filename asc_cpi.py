import numpy as np
from bs4 import BeautifulSoup

f = open('asc.html')
grade_dict = {'AA': 10, 'AB': 9, 'BB': 8, 'BC': 7,
              'CC': 6, 'CD': 5, 'DD': 4, 'FR': 0, 'PP': 1}

soup = BeautifulSoup(f, 'html.parser')

l = []
for i in soup.findAll('table', {'class': 'ss'}):
    for j in i.findAll('td'):
        l.append(j.text)

# for i in l[1::6]:
    # print(i)


def cpi(l):
    my_cpi = 0
    total_credits = 0
    for i, j in zip(l[2::6], l[4::6]):
        if j.strip() == 'FR':
            continue
        my_cpi += float(i) * float(grade_dict[j.strip()])
        total_credits += float(i)
        print(float(i) , float(grade_dict[j.strip()]))
    my_cpi = my_cpi/total_credits
    print(total_credits)
    print(my_cpi)
    return my_cpi
cpi(l)
print(len(l[::6]))