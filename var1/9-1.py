count = 0
f = open('9-1.txt')
for s in f:
    arr = [int(i) for i in s.split()]
    rep = sum(arr) - sum(set(arr))
    mean_unrep = sum(set(arr) - {rep}) / 4
    if len(set(arr)) == 5 and mean_unrep <= 2 * rep:
        count += 1
print(count)
# 1 1 2 3 4 5 -> 1 2 3 4 5 -> 2 3 4 5 
# 1 2 
# 1 1 1 1 4 5 -> mean - ??? -> len(set(arr)) == 5
# 

