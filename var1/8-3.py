from itertools import *
c = 1
for x in range(1, 11):
    for w in permutations("0123456789", r = x):
        if w[0] != "0" and int("".join(w)) % 5 == 0:
            c += 1

print(c)