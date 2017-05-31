from random import randint
from multiprocessing.dummy import Pool as ThreadPool 

## Winning Probability For calling higher
## my dice sum will be higher than shop's
 
win=loose = 0
def fun(j):
	global win
	global loose
	for i in range(100000*j):

		l = [randint(1,6) for j in range(4)]
		if (l[0] + l[1] ) > (l[2] + l[3]):
			win = win + 1
		else:
			loose = loose+ 1

# for i in range(10000000):
# 	l = [randint(1,6) for j in range(4)]
# 	if (l[0] + l[1] ) > (l[2] + l[3]):
# 		win += 1
# 	else:
# 		loose += 1


with ThreadPool(20) as pool:
    results = pool.map(fun,[1 for i in range(19)])


print(win+loose , win,loose,win/(win+loose))