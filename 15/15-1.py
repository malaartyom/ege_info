# ((x<6)→(x2 <A))∧((y2 ≤A)→(y≤6))
from tqdm import tqdm
counter = 0
for A in tqdm(range(1000)):
    flag = True
    for x in range(1000):
        for y in range(1000):
            if not(((x < 6) <= (x ** 2 < A)) and ((y ** 2 <= A) <= (y <= 6))):
                flag = False
                break
    if flag:
        counter += 1

print(counter)