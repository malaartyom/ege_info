counter = 0
alph = 'АБРТЫ'
for x1 in alph:
    for x2 in alph:
        for x3 in alph:
            for x4 in alph:
                for x5 in alph:
                    flag = 0
                    total = x1 + x2 + x3 + x4 + x5
                    counter += 1
                    if total.count('Ы') == 0:
                        # for i in range(len(total)-1):
                        #     if total[i] != 'А' and total[i+1] != 'А':
                        #         print(counter)
                        for i in range(len(total) - 1):
                            if total[i] == "А":
                                if total[i + 1] == "А":
                                    flag = 1
                        if flag == 0:
                            print(total, counter)
                            break
#ABAAA
# 


print(counter)

