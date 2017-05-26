import matplotlib.pyplot as plt
import matplotlib.animation as anim
from matplotlib import style
import random
from mpl_toolkits.mplot3d import axes3d
import numpy as np
import csv

file = open('aa.csv','r')
reader = csv.reader(file)
for row in reader:
    pass
    break

x = [i for i in range(1,25)]
y = [[] for i in range(7)]

ct = 0


for row in reader:
    print(ct)
    for i in range(len(row)):
        if '#DIV/0!' in row[i]:
            row[i] = 0
    tmp = []
    for i in range(34,55):
        tmp.append(row[i])
    #print(tmp)
    #print(len(tmp))
    row_n0 = 0
    t = 0
    for i in range(7):
        y[t].append((float(tmp[row_n0]) + float(tmp[row_n0+1]) + float(tmp[row_n0+2]))/3)
        row_n0 += 3
        t+=1
    ct += 1
    if ct == 24:
        break
print(y)
print(len(y[0]))

for i in range(7):
    plt.plot(x,y[i])
plt.show()
plt.legend()