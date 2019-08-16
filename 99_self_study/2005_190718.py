T = int(input())

 
for i in range(T):
    row = int(input())
    buffer = []
    print('#%d' %(i+1))
    for j in range(row):
        memory = buffer
        buffer = buffer + [1]
        for k in range(1, j):
            buffer[k] = memory[k-1] + memory[k]
        for n in range(len(buffer)):
            print(buffer[n], end=' ')
        print()