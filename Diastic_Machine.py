

fin = open('big.txt','r')

seed = "My name is crusoe"

seed = (seed.lower()).replace(' ','')

ct = 1
end = 0
ans = ''
for i in fin :

    l = i.split(" ")
    for j in l:
        
        j = j.lower()
        if j.isalpha():
            if len(j) <= ct-1:
                continue
            else:
                if j[ct-1] == seed[ct-1]:
                    #print(j)
                    ans += j + " "  
                    if ct == len(seed):
                        end = 1
                        break
                    ct += 1
                    
    if end:
        break

print(ans)