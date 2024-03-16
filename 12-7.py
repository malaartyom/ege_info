def prime(n):
    if n <= 1:
        return False
    for i in range (2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
# r = 0
for n in range(101, 1000):
    r = 0
    s = '0' + '2' * 50 + '1' * n + '0'
    s1 = s
    while "00" not in s:
        s = s.replace('02','101', 1)
        s = s.replace('11', '2', 1)
        s = s.replace('012', '30', 1)
        s = s.replace('010', '00', 1)
    for i in range(len(s)):
        r = r + int(s[i])
    if prime(r):
         print(n)