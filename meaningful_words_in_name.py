import itertools

name = 'dog'

l = list(name)
permut_words = []
for i in range(2,len(l)+1):
    permut_words.extend([list(j) for j in itertools.permutations(l,i)])


f = open('/usr/share/dict/american-english','r')
words = [i.strip() for i in f]


for j in permut_words:
    s = ''
    for i in j:
        s+=i
    if s in words:
        print(s)
