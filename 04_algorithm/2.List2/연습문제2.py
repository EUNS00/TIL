data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
#
for i in range(1, 1<< len(data)):
    sum = 0
    for j in range(len(data)):
        if i & (1<<j): sum += data[j]

    if sum == 10:
        for j in range(len(data)):
            if i & (1<<j):
                print(data[j], end=" ")
        print()