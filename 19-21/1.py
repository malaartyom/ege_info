# Ходы +1 +2 or *
# >= 47 WIN
# 1<= S <= 37

from functools import lru_cache

def moves(h):
    a, b = h
    return (a + 1, b + 2), (a + 2, b + 1), (a * 2, b), (a, b * 2)

@lru_cache(None)
def game(h):
    if sum(h) >= 47:
        return "W"
    if any(game(m) == "W" for m in moves(h)):
        return "P1"
    if any(game(m) == "P1" for m in moves(h)):
        return "B1"
    if any(game(m) == "B1" for m in moves(h)):
        return "P2"
    if all(game(m) == "P1" or game(m) == "P2" for m in moves(h)):
        return "B2"

for s in range(1, 37):
    if game((10, s)) is not None:
        print(s, game((10, s)))
        