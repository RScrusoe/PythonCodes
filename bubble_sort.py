## bubble sort
import random
import time

l = [random.random() for i in range(10000)]



def bubble_sort(l):
	ans = []
	for i in l:
		flag = 0
		for j in range(len(ans)):
			if i<=ans[j]:
				ans.append(ans[len(ans)-1])
				for x in range(len(ans)-2,j,-1):
					ans[x] = ans[x-1]
				ans[j] = i
				flag = 1
				break
		
		if not flag:
			ans.append(i)
	return ans
		

t1 = time.time()
ans = bubble_sort(l)
t2 = time.time()
print("Time for bubble sort : " + str(t2-t1))

t1 = time.time()
l.sort()
ans = l
t2 = time.time()
print("Time for inbuilt sort : " + str(t2-t1))
