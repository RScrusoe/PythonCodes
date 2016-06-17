import matplotlib.pyplot as plt
import matplotlib.animation as anim
from matplotlib import style
import random
from mpl_toolkits.mplot3d import axes3d

import numpy as np
style.use('fivethirtyeight')
fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')
#ax2 = fig.add_subplot(212,projection='3d')
x = []
y = []
a = int(1)
y2 = []
x2 = []
def animate (i):


    y.append(random.random())
    y2.append(random.random())

    global a
    x.append(a)
    x2.append(a)
    a+=1
    ax1.clear()
    ax1.plot(x,y,'-')
    ax1.plot(x2,y2,'-')

#ani = anim.FuncAnimation(fig,animate,1000)
x3 = [1,2,3,4,5,6,7,8,9,10]
y3 = [3,6,3,6,5,1,7,0,3,5]
z3 = np.zeros(10)
z4 = [2,4,4,3,1,9,6,7,3,9]
dx = np.ones(10)
dy = dx
dz = y3


ax1.set_xlabel('x axis')
ax1.set_ylabel('y axis')
ax1.set_zlabel('z label')
ax1.bar3d(x3,y3,z3,dx,dy,dz)

ax1.scatter(x3,y3,z4 , color='r',marker='*')
ax1.plot_wireframe(x3,z4,y3,color='k')

plt.show()