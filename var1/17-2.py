with open("17-2.txt") as file:
    data = [int(i) for i in file]
    answer = []
    for i in range(len(data) - 1):
        for j in range(i + 1, len(data)):
            if abs(data[i] - data[j]) % 2 == 0 and (data[i] % 31 == 0 or data[j] % 31 == 0):
                answer.append(data[i] + data[j])
    
    print(len(answer), max(answer))
            
