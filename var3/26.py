#7291 3490
size = 7291
users = []
with open('28140.txt', 'r') as f:
    # f = [int(i[:-1]) for i in f.readlines()[1:]]
    f = [int(i) for i in f.readlines()[1:]] # <---- вот это правильный вариант. Тут ты зачем то обрезал последнюю цифру числа. А нужно обрезать только f.readlines()
    # теперь всё работает правильно
    f.sort()
    summ = 0
    counter = 0
    for i in range(len(f)):
        if summ + f[i] > size:
            break
        summ += f[i]
    # new_users = users[:-1]
    # summ = summ - users[-1]
    print(i)
    print(summ)


# 7274

f = open('28140.txt')
data = f.readlines()
s = data[0].split()
s = int(s[0])
del (data[0])  # первая строка больше не нужна, удаляем ее
for i in range(0, len(data)):
    data[i] = int(data[i])
data = sorted(data)
summa = 0
for count in range(0, len(data)):
    if summa + data[count] > s: break
    summa += data[count]
print(count)
print(summa)
zapas = s - summa
for i in range(0, len(data)):
    if data[i] - data[count - 1] <= zapas:
        itog = data[i]
print(itog)