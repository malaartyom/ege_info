s = open('24.txt').readline().split('D')[1:-1]
mx = 0
count = 1
for i in range(len(s)):
    if s[i].count('O') <= 2:
        count += len(s[i]) + 1 
        mx = max(mx, count)
    else:
        count = 1
print(mx)