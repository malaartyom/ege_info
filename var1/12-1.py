# НАЧАЛО
#                 ПОКА нашлось (01) ИЛИ нашлось (02)
#                         заменить (02, 1110)
#                         заменить (01, 220)
#                 КОНЕЦ ПОКА
# КОНЕЦ
def div(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
s = "1" * 10
mini = 1000000
for x in range(100):
    for y in range(100):
        s = '0' + '1'* x + '2'* y
        if len(s) > 44:
            while ('01' in s) or ('02' in s):
                s = s.replace('02','1110', 1)
                s = s.replace('01','220', 1)
            if div(s.count('1') + s.count('2') * 2):
                mini = min(mini,x + 2*y)
print(mini)

# y - 2   y * 2