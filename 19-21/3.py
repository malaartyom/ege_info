# # +2 +1 +1 +2 *2
# # 1 <= s <= 36
# # >= 47 - win

# from functools import lru_cache
# def moves(h):
#     a, b = h
#     return (a + 2, b + 1), (a + 1, b + 2), (a * 2, b), (a, b * 2)

# @lru_cache(None)
# def game(h):
#     if sum(h) >= 47:
#         return "W"
#     if any(game(m) == "W" for m in moves(h)):
#         return "П1"
#     if all(game(m) == "П1" for m in moves(h)):
#         return "B1"
#     if any(game(m) == "B1" for m in moves(h)):
#         return "П2"
#     if all(game(m) == "П1" or game(m) == "П2" for m in moves(h) ):
#         return "B2"
    
# for s in range(1, 37):
#     if game((10, s)) is not None:
#         print(s, game((10, s)))

with open("17-1.txt", "r") as file:
    s = file.read().splitlines()
    
    
f = open("17-1.txt", "r")

f.close()


