
ct = 1
global l
l = []
sum_list = []
def p(head,tail=''):
	if len(head) == 0:
		#print(tail)
		l.append(tail)
	else:
		for i in range(len(head)):
			p(head[0:i] + head[i+1:] ,tail + head[i])
			
p('123456789')

for i in l:
	frac_list = []
	#print(ct)
	j = 0
	while(j<=6):
		frac_list.append(int(i[j])/(int(i[j+1])*10 + int(i[j+2])))
		j+=3
	sum_list.append(sum(frac_list))
	#print(frac_list)
	#if sum(frac_list) >= 0.999 and sum(frac_list) <= 1.001 :
	if sum(frac_list) ==1:
		print("the combination is  " + str(i))	
		 	
	ct+=1
	#if ct == 10:
	#	break

#print(max(sum_list))
