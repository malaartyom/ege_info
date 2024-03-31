# #x & 49 = 0 → (x & 28 ≠ 0 → x & А ≠ 0)
# a = []
# for A in range(1000):
#     flag = True
#     for x in range(1000):
#         if not((x & 49 == 0) <= ((x & 28 != 0) <= (x & A != 0))):
#             flag = False
#             break
#     if flag:
#         a.append(A)

# print(a)



# x & 49 = 0 → (x & 28 ≠ 0 → x & А ≠ 0)

# a - min
a = []
for A in range(1000):
    flag = 1
    for x in range(1000):
        if not((x & 49 == 0) <= ((x & 28 != 0) <= (x & A != 0))):
            flag = 0
            break
    if flag:
        print(A)
        a.append(A)

print(a)