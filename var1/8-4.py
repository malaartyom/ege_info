from itertools import *
a = "012345"
c = 0
for i in product(a, repeat = 3):
    if int(i[0]) >= int(i[1]) and int(i[1]) >= int(i[2]):
        c += 1
        print(i)
print(c - 1)
