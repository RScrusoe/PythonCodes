from rohan import *

n = 5
# l = [i for i in itertools.combinations([j for j in range(64)],n)]

def isConflict(x):
    for i in range(n):
        for j in range(i+1,n):
            if int(x[i]/8) == int(x[j]/8):
                return False
            elif x[i]%8 == x[j]%8:
                return False
            elif (x[i]- x[j])%9 == 0:
                return False
            elif (x[i]- x[j])%7 == 0:
                return False
    return True


# for i in [8*k for k in range(8)]:
#     print([i+j for j in range(8)])
#     i+=8


ans = []
for i in itertools.combinations([j for j in range(64)],n):
    if isConflict(i):
        ans.append(i)


# for i in l:
#     if isConflict(i):
        # ans.append(i)

print('N = {} | Possibilities = {}  |  #noConflict = {}  | Fraction = {}'.format(n,len(l),len(ans),len(ans)/len(l)))


# N = 1 | Possibilities = 64        |  #noConflict = 64     | Fraction = 1.0
# N = 2 | Possibilities = 2016      |  #noConflict = 1128   | Fraction = 0.5595238095238095
# N = 3 | Possibilities = 41664     |  #noConflict = 6796   | Fraction = 0.16311443932411673
# N = 4 | Possibilities = 635376    |  #noConflict = 14246  | Fraction = 0.022421369393870717
# N = 5 | Possibilities = 7624512   |  #noConflict = 9592   | Fraction = 0.001258047728169357