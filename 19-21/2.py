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

@lru_cache(None)   
def game(h):
    #any 
    #all / any
    #any
    #all ... 
    
    pass

for s in range():