def d(n, m):
    return n % m == 0
#¬ДЕЛ(x, А) → (¬ДЕЛ(x, 21) ∧¬ ДЕЛ(x, 35))
a = []
for A in range(1, 1000):
    for x in range(1, 1000):
        flag = True
        if not((not(d(x, A))) <= ((not(d(x, 21))) and (not(d(x, 35))))):
            flag = False
            break
    if flag:
        a.append(A)

print(a)
