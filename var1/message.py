# НАЧАЛО
# ПОКА нашлось (12) ИЛИ нашлось (322) ИЛИ нашлось (222)
#   ЕСЛИ нашлось (12)
#     ТО заменить (12, 2)
#   КОНЕЦ ЕСЛИ
#   ЕСЛИ нашлось (322)
#     ТО заменить (322, 21)
#   КОНЕЦ ЕСЛИ
#   ЕСЛИ нашлось (222)
#     ТО заменить (222, 3)
#   КОНЕЦ ЕСЛИ
# КОНЕЦ ПОКА
# КОНЕЦ
n2 = 0
for n in range(4, 1000):
    s = '1' + '2'*n
    while ('12' in s) or ('322' in s) or ('222' in s):
        if '12' in s:
            s = s.replace('12', '2', 1)
        if '322' in s:
            s = s.replace('322', '21', 1)
        if '222' in s:
            s = s.replace('222', '3', 1)
    n1 = len(s)
    if n1 > n2:
        n2 = n1
    n1 = 0
print(n2)