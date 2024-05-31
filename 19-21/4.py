from functools import lru_cache
# 84 - WIN
def moves(h):
    a, b = h
    if h % 2 == 0:
        return (a +1, b + 1), (a * 2, b * 3)
    else:
        return h * 2, h + 1
    
@lru_cache(None)
def game(h):
    if h >= 84:
        return "W"
    if any(game(m) == "W" for m in moves(h)):
        return "P1"
    if all(game(m) == "P1" for m in moves(h)):
        return "B1"
    if any(game(m) == "B1" for m in moves(h)):
        return "P2"
    if all(game(m) == "P1" or game(m) == "P2" for m in moves(h)):
        return "B2"

for s in range(1, 84):
    if game(s) is not None:
        print(s, game(s))