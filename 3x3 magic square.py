
global l
l = []

def p(head,tail=''):
	if len(head) == 0:
		#print(tail)
		l.append(tail)
	else:
		for i in range(len(head)):
			p(head[0:i] + head[i+1:] ,tail + head[i])
			
p('123456789')

for i in l:
	matrix = []
	for j in range(3):
		matrix.append([int(x) for x in i[j*3:j*3+3]])
	#print(matrix)
	m_sum = [sum(x) for x in matrix]
	
	inv_matrix = []
	for j in range(3):
		inv_matrix.append([int(i[j]),int(i[j+3]),int(i[j+6])])
	iv_sum = [sum(x) for x in inv_matrix]

	if m_sum == iv_sum:
		if all(x == m_sum[0] for x in m_sum):
			x1 = sum([x[z] for z,x in enumerate(matrix)])
			#print(matrix)
			#print(x1)
			x2 = sum([x[z] for z,x in enumerate([ matrix[len(matrix) - j - 1] for j in range(len(matrix))])])
			if x1 == x2 == m_sum[0]:
				print(i)
				

