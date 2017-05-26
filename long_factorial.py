def long_factorial(n):
	prev = [1]
	carry = 0
	for i in range(2,n+1):
		ans = []
		
		for j in range(len(prev)):
			prod = i*prev[j] +carry
			ans.append(prod%10)
			carry = int(prod/10)
		while carry is not 0:
			ans.append(carry%10)
			carry = int(carry/10)

		prev = ans

	return(ans[::-1])

print(long_factorial(20))
'''
def factoraial(n):
	x  = 1
	for i in range(1,n+1):
		x*=i
	return x

x=''
for j in long_factorial(20):
	x+=str(j)
print(x)
print(factoraial(20))

'''
