t = int(input())
t=int(t)
while t>0:
    n = int(input())
    n=int(n)
    l=[]
    while(n>0):
        if(n==0):
            break
        if(n%2==0):
            n=int(n/2)
            l.append('0')
        else:
            n=int(n/2)
            l.append('1')
        #print(n)
    l.reverse()
    for i in l:
        print(i,end='')
    print()
    #print ('%s' % ''.join(map(str, l)))
    
    
    t=t-1