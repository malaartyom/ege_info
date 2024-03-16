p1, p2, q1, q2 = 5, 30, 14, 23

P = [i/10 for i in range(p1*10, p2*10+1)]
Q = [i/10 for i in range(q1*10, q2*10+1)]

def f(A, x):
    return ((x in P) == (x in Q)) <= (not(x in A))

A = set([i/10 for i in range(40,321)])

for x in [i/10 for i in range(40,321)]:
    if not f(A, x):
        A.remove(x)
print(sorted(A))