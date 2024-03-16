for x in "0123456789ABCD":
    y = (int("1" + x + "563", 14) + int("871" + x + "3", 14))
    if y % 24 == 0:
        print(x, y // 24)


