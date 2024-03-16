def A22(x, y):
    if x == y:
        return 1
    if x > y:
        return 0
    return A22(x + 1, y) + A22(x + 2, y) + A22(x + x - 1, y)

print(A22(2, 9))

    