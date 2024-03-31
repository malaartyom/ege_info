for a in range(10 ** 5):
    flag = 1
    for x in range(10 ** 5):
        if ((x & 20777 != 0) <= ((x & 12332 == 0) <= (x & a != 0))) == 0:
            flag = 0
            break
    if flag == 1:
        print(a)

# for a in range(0, 10**5): 
#     k = True
#     for x in range(0, 10**5):
#         if ((x & 20777 != 0) <= ((x & 12332 == 0) <= (x & a != 0)))==0:
#             k = False
#             break
#     if k == True:
#         print(a)
#         break
            
# or and -> not