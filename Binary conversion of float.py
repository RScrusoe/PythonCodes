x = float(input("Enter a number to convert into Binary"))
p=0
while((((2**p)*x)%1)!=0):
    print("Remainder is " + str(((2**p)*x)-int(((2**p)*x))))
    p+=1
#print(p)
num = int(((2**p)*x))
result = ' '
#print(num)

if num ==0:
    result = '0'
while(num >0):
    tmp = num % 2
    l=str(tmp)
    #print(l)
    result = l +result
    num = int(num/2)

#print(str(result))
for i in range(p-(len(result))+1):
    result='0'+result
#print("@@@@@@@@@@@@@@")

tmpl = len(result)
#print(result[0:(tmpl-p)])
#print(result[(tmpl-p):])
if tmpl-p ==0:
    result = '.'+result
else:
    result = result[0:(tmpl-p)]+'.'+result[(tmpl-p):]
print(result)
print("Binary form of "+ str(x)+ " is "+  result)
