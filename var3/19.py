from functools import *
# Принимает кол-во на данном ходе
# Выдает все возможные ходы из этой кучи

# Если несколько кучек, то передаешь набор кучек
def moves(n):
    # a, b = n
    # print(a)
    # print(b)
    if n == 1:
        return [2]
    for k in range(2, n + 1):
        if n%k == 0:
            a.append(n + n // k)
    return a
# # Функция котрая описывает нашу игру
# # Принимает кол-во на данном ходе и выдает выигрышные ходы

@lru_cache(None)
def game(h):
    if h > 40:
        return 'Win'
    if any(game(i) == 'Win' for i in moves(h)):
        return 'П1'
    if all(game(i) == 'П1' for i in moves(h)):
        return 'В1'
    if any(game(i) == 'В1' for i in moves(h)):
        return 'П2'
    if all(game(i) == 'П2' or game(i) == "П1" for i in moves(h)):
        return 'В2'


for i in range(1, 41):
    if game(i) is not None:
        print(game((10, i)), i)
# # set, list< dict, tuple (1, 3)
#
#
# moves((10, 15))
