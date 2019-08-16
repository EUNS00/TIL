l = 5
p = 0

for i in range(l):
    for I in range(l):
        if i == I:
            print('#', end='')
        elif i != I:
            print('+', end='')
    print('')