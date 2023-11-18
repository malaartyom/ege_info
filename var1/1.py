for n in range(10**10+1):
    for i in range(10):
        x = str('1') + str(i) + str('2139') + str(n) + str('4')
        if (int(x)%2023) == 0 and int(x) < 10**10:
            print(x, int(x)//2023)


# https://inf-ege.sdamgia.ru/problem?id=37336

# https://inf-ege.sdamgia.ru/problem?id=37340

# https://inf-ege.sdamgia.ru/problem?id=37345