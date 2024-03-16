#x & 49 = 0 → (x & 28 ≠ 0 → x & А ≠ 0)
a = []
for A in range(1000):
    flag = True
    for x in range(1000):
        if not((x & 49 == 0) <= ((x & 28 != 0) <= (x & A != 0))):
            flag = False
            break
    if flag:
        a.append(A)

print(a)
