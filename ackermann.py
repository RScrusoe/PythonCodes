import time
import sys
sys.setrecursionlimit(15000)
print(sys.getrecursionlimit())
l = []

def ack (m,n):
	for i in l:
		if (i[0] == m) and  (i[1] == n):
			return i[2]
	ans = 0
	if (m == 0):
		ans = n+1
	elif (n == 0):
		ans = ack(m-1,1)
	else:
		x = ack(m,n-1)
		l.append([m,n-1,x])
		ans = ack(m-1, x)
	return (ans)



for i in range(5):
	
	for j in range(5):
		t = time.time()
		a = ack(i,j)
		print(str(a) + "  || ", end="")
		l.append([i,j,a])
		print(time.time()-t)
print(l)
