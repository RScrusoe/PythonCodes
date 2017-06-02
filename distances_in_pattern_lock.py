import itertools as it

l = [list(i) for i in it.permutations([1,2,3,4,5,6,7,8,9])]


def dist(x,y):
	ix = int((x-1)/3)
	jx = int((x-1)%3)
	iy = int((y-1)/3)
	jy = int((y-1)%3)
	#print(ix,jx,iy,jy)
	if ix  == iy:
		return abs(jx-jy)
	elif jx == jy:
		return abs(ix-iy)
	elif (abs(ix-iy)==1) and (abs(jx-jy)==1):
		return 1.414
	elif (abs(ix-iy)==1) and (abs(jx-jy)==2):
		return 2.236
	elif (abs(ix-iy)==2) and (abs(jx-jy)==1):
		return 2.236
	elif (abs(ix-iy)==2) and (abs(jx-jy)==2):
		return 2.828

distances = []
for i in range(len(l)):
	d = 0
	for j in range(8):
		d = d + dist(l[i][j],l[i][j+1])
		#print(l[i][j],l[i][j+1],d)
	# if maxi<d:
	# 	maxi=d
	if d not in distances:
		distances.append(d)
	l[i].append(d)
distances.sort()
print(distances)