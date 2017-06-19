from rohan import *
from subprocess import call
import subprocess

# n = int(input().strip())
# l = list(map(int,input().strip().split(' ')))
#F090866
x = 4373612677928697257861252602371390152816537558161613618621437993378423467772036
y = 36875131794129999827197811565225474825492979968971970996283137471637224634055579
z = 154476802108746166441951315019919837485664325669565431700026634898253202035277999
t1 = time.time()
ans = x/(y+z) + y/(x+z) + z/(x+y)
print(time.time())



#call(['python3', 'marathi_dictionary_khandbahale.py'])
import os
cmd = 'gpg aa.gpg'
#os.system(cmd)


#fyjc:
#417849
#ROHAN1



import sys



# n = int(input().strip())
# unsorted = [5,2,7]
# unsorted_i = 0
# for unsorted_i in range(n):
#    unsorted_t = str(input().strip())
#    unsorted.append(unsorted_t)
# your code goes here


n=100
l = [random.randint(0,99) for i in range(100)]
print(l)
d={}
for i in range(0,100):
    d[i]=0
#print(d)
for i in l:
    d[i] +=1

for i in d.keys():
    print(d[i],end=" ")

f = open('zip','a')
for i in range(100000000):
    f.write('0')
f.close()