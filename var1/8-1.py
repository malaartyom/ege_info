from itertools import *
counter = 0
for word in product("ABCX", repeat=5):
    if (word.count("X") == 0) or (word[0] == "X" and word.count("X") == 1):

        counter += 1

print(counter)