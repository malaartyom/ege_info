with open("17.txt", "r") as file:
    data = [int(i) for i in file]
    answer = []
    for i in range(1, len(data)):
        if data[i - 1] % 3 == 0 or data[i] % 3 == 0:
            answer.append(data[i -1] + data[i])

    print(len(answer), max(answer))