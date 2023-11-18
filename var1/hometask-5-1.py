for i in range(10000, 1000, -1):
    s = str(i)
    k1 = int(s[0]) + int(s[1])
    k2 = int(s[1]) + int(s[2])
    k3 = int(s[2]) + int(s[3])
    first = str(max(k1, k2, k3))
    second = str(k1 + k2 + k3 - max(k1, k2, k3) - min(k1, k2, k3))
    s1 = second + first
    if s1 == '1515':
        print(i)
        break