# 2
print('x y z w f f2')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f1 = (x or not(y)) == (z <= w)
                f2 = (not(x) == y) and (z <= w)
                print(x, y, z, w, int(f1), int(f2))

# 0 1 0 0 0 1

