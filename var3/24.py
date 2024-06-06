idx = []
substr_len = []
with open("24_1.txt", "r") as f:
    f = f.readline()
    for i in range(len(f)):
        if f[i] == "T":
            idx.append(i)
    print(idx[:10])
    for i in range(len(idx) - 99):
        substr_len.append(idx[i + 99] - idx[i] + 1)
    print(min(substr_len))
