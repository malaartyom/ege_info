# # ((x<6)→(x2 <A))∧((y2 ≤A)→(y≤6))
# from tqdm import tqdm
# counter = 0
# for A in tqdm(range(1000)):
#     flag = True
#     for x in range(1000):
#         for y in range(1000):
#             if not(((x < 6) <= (x ** 2 < A)) and ((y ** 2 <= A) <= (y <= 6))):
#                 flag = False
#                 break
#     if flag:
#         counter += 1

# print(counter)


# ((x<6)→(x2 <A))∧((y2 ≤A)→(y≤6)) 

from tqdm import tqdm 
counter = 0
for A in tqdm(range(300)):
    flag = True
    # 7
    for x in range(300):
        for y in range(300):
            # x = 12 y = 56
            if not(((x < 6) <= (x ** 2 < A)) and ((y ** 2 <= A) <= (y <= 6))):
                flag = False
                break
    if flag:
        counter += 1
    
print(counter)








# 1001
# 0101
#     &
# 0001








