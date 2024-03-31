from functools import lru_cache
def moves(h):
    if h % 2 == 0 and h % 3 == 0:
        return h + 1, h + h // 2, h + h // 3
    elif h % 2 == 0 and h % 3 != 0:
        return h + 1, h + h // 2
    elif h % 2 != 0 and h % 3 == 0:
        return h + 1, h + h // 3
    elif h % 3 != 0 and h % 2 != 0:
        return h + 1, h * 2
# 96 - win
# 1 <= s <= 95
@lru_cache(None)
def game(h):
    if h >= 96:
        return "W"
    if any(game(m) == "W" for m in moves(h)):
        return "P1"
    if any(game(m) == "P1" for m in moves(h)):
        return "В1"
    if any(game(m) == "В1" for m in moves(h)):
        return "P2"
    if all(game(m) == "P2" or game(m) == "P1" for m in moves(h)):
        return "B2"

for s in range(1, 96):
    if game(s) is not None:
        print(s, game(s))