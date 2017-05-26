import sys
sys.setrecursionlimit(5000000)

# Algo is here https://www.quora.com/How-would-you-explain-an-algorithm-that-generates-permutations-using-lexicographic-ordering


def swap(a,x,y):
	tmp = a[x]
	a[x] = a[y]
	a[y] = tmp
	return a

ct = 0
l = [1,5,2,4,9,3]
l.sort()

# For total permutations use sorted list

def permute(l):
	global ct
	ct+=1
	largestX= -1

	for i in range(len(l) - 1):
		
		if l[i] < l[i+1]:
			largestX = i
	
	if largestX == -1:
		print('Finished with total count = ' + str(ct))
		return
	
	largestY = -1
	for j in range(largestX,len(l)):
		if l[largestX] < l[j]:
			largestY = j
	
	l = swap(l,largestX,largestY)

	nl = l[:largestX+1]

	nl += l[largestX+1:][::-1]

	print(nl)
	permute(nl)

permute(l)





