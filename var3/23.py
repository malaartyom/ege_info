global c
c = 1


def g(a):
    global c
    c += 1
    if c >= 2:
        return 10 ** 10
    else:
        return a - 1


def k(a):
    global c
    if c > 0:
        c -= 1
    return a * 2


def y(a):
    global c
    if c > 0:
        c -= 1
    return a * 3


def f(a, b):
    # global c
    # c -= 1
    if a == b:
        return 1
    if a > b:
        return 0
    if a < b:
        return f(g(a), b) + f(k(a), b) + f(y(a), b)


print(f(3, 20))
