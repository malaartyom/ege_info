from itertools import *
counter1 = 0

#012345678
for number in product("012345678", repeat = 7):
    counter2 = 0 # лучше обнулять в начале, когда мы только наиснаем обрабатывать новое число
    counter3 = 0
    if number[0] != "0": # тут if тоже лучше чуть выше вынести чтобы он сначала смотрел на условие,
                         # а только потом проходился по самому числу
        for i in range(7):# <-- 7 вместо 6
            if number[i] == "6":
                counter2 += 1
            if int(number[i])%2 == 1:
                counter3 += 1
        if counter2 == 1 and counter3 == 2: # <- главная проблема была тут, нужно было 
            counter1 += 1                   #    проверять это услвоие вне цикла, а ты проверял внутри
print(counter1)

# в целом молодец, идея была правильная. Этот номер ещё посмотрим на паре.
            