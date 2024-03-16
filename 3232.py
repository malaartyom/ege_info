from math import comb
from itertools import product

print(comb(16, 3))
print(len(range(237567900, 1134567011, 10)))

print(str(4 * 6 ** 20))
print
print(4 * 6 ** 20 < int("8" +"000" + "8" * 13, 9) < 5 * 6 ** 20)
print(121 - 14 * 8)


counter = 0 
for i in product("012345678", repeat = 3):
    if sum([int(j) for j in i]) == 9:
        counter += 1
print(counter)
print(counter * comb(16, 3))
    
