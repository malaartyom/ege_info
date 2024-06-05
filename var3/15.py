# p1, p2, q1, q2, r1, r2 = 24, 77, 47, 92, 82, 116
# P = [i/10 for i in range(p1*10, p2*10+1)]
# Q = [i/10 for i in range(q1*10, q2*10+1)]
# R = [i/10 for i in range(r1*10, r2*10+1)]
#
# def f(x, A):
#     return ((not((x in Q) <= ((x in P)or(x in R)))) <= ( (not(x in A)) <= (not(x in Q)) ) )
#
# A = set()
#
# for x in range(230, 1170):
#     y = x / 10
#     if not f(y, A):
#         A.add(y)
# print(sorted(A))
# print(list(range(230, 1170)))


p1, p2, q1, q2, r1, r2 = 24, 77, 47, 92, 82, 116
P = [i / 10 for i in range(p1 * 10, p2 * 10 + 1)] #
Q = [i / 10 for i in range(q1 * 10, q2 * 10 + 1)] #
R = [i / 10 for i in range(r1 * 10, r2 * 10 + 1)] #


def f(x, A):
    return (not((x in Q) <= ((x in P) or (x in R)))) <= ((x not in A) <= (x not in Q)) # ----


A = []
z =  [i / 10 for i in range(230, 116 * 10 + 3)]

for x in [i / 10 for i in range(23 * 10, 117 * 10)]:  # -----
    if not f(x, A):
        A.append(x)
print(sorted(A))
print(len(A))

# list, set, dict, ....
