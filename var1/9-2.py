cnt = 0
f = open('9-2.txt')
for s in f:
    a = list(map(int,s.split()))
    a.sort()
    if a[0]*a[2] + a[0]*a[1] < a[1]*a[2]:
        cnt+=1
print(cnt)

