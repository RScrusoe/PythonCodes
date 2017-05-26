import csv

f = open('mess.csv','r')
reader = csv.reader(f)
g = open('bill.csv','w')
l = []
for i in reader:
	x = [i[0],i[16]]
	l.append(x)

l.pop()
l.pop(0)
x = [int(i[0]) for i in l]
print(x)
for i in range(1,395):
	if int(i) not in x:
		row = [int(i),int(0)]
	else:
		for j in l:
			if int(j[0]) == i:
				row = j
				break
	g.write(str(row[0]) + ',' + str(row[1]) + '\n')

f.close()
g.close()