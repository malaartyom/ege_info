# НАЧАЛО
#     ПОКА нашлось (111)
#         заменить (111, 22)
#         заменить (222, 11)
#     КОНЕЦ ПОКА
# КОНЕЦ

strng = '1' * 99
while ('111' in strng):
    strng = strng.replace('111', '22', 1)
    strng = strng.replace('222', '11', 1)
print(strng)