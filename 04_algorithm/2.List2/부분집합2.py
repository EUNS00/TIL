data = [1, 2, 3]

n = len(data)

for i in range(1<<n):
    for j in range(n):
        if i & (1<<j):
            print(data[j], end=" ")
    print()
print()