alph = "АКРУ"
counter = 1
for i1 in alph:
    for i2 in alph:
        for i3 in alph:
            for i4 in alph:
                for i5 in alph:
                    w = i1 + i2 + i3 + i4 + i5
                    if w == "РУКАА":
                        print(counter)
                    counter += 1
