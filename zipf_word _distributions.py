from matplotlib import pyplot as plt

### OPEN ANY NOVEL AS 'r'
f = open('tale.txt','r')
###


l = []
flag = 0
for i in f:
    #print(i)
    i = i.split()
    for j in i:
        flag = 0
        j = str(j).replace(" ",'').replace(",",'').replace(".",'')
        if j.isalpha():
            #print(j)
            for k in l:
                if k[0] == j:
                    k[1] += 1
                    flag = 1
                    break
            if not flag:
                l.append([j,1])
                
l.sort(key=lambda x: x[1])
words = [i[1] for i in l][::-1][:150]
plt.plot([i for i in range(1,len(words)+1)],words)
plt.show()
#print(l)