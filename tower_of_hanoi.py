from rohan import *
l = []
def move_disks(n, source, intermediate, destination):
    if n > 1:
        move_disks(n - 1, source, destination, intermediate)
        move_disks(1, source, intermediate, destination)
        move_disks(n - 1, intermediate, source, destination)
    else:
        l.append(" {} -> {}".format(source,destination))

move_disks(3,'A','B','C')

for i in l:
    print(i)

