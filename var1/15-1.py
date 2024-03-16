# D  =  [17; 58] и C  =  [29; 80]. 

# (x ∈ D) → ((¬(x ∈ C)∧ ¬(x ∈ A)) → ¬(x ∈ D))

d1, d2, c1, c2 = 17, 58, 29, 80

D = [i / 10 for i in range(d1 * 10, d2 * 10 + 1)]
C = [i / 10 for i in range(c1 * 10, c2 * 10 + 1)]

def f(x, A):
    return (x in D) <= ((not(x in C) and not(x in A)) <= (not(x in D)))

A = set()
for x in [i / 10 for i in range(100, 901)]:
    if not f(x, A):
        A.add(x)
print(sorted(A))
