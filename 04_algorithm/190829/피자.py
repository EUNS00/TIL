import sys
sys.stdin = open("피자.txt")

T = int(input())

for tc in range(1, T+1):
    result = []
    pizza = []
    stat = 0
    N, M = map(int, input().split())
    ci = list(map(int, input().split()))
    for num, i in enumerate(ci):
        result.append([num+1, i])

    while len(result) != 0:
        if len(pizza) < N:
            if len(result) != 0:
                pizza.append(result.pop(0))

        if len(pizza) == N:
            a = pizza.pop(0)
            if a[1] > 0:
                a[1] = a[1]//2
                if a[1] == 0:
                    pizza.append(result.pop(0))
                else:
                    pizza.append(a)



    while len(pizza) != 1:
        a = pizza.pop(0)
        if a[1] > 0:
            a[1] = a[1] // 2
            if a[1] != 0:
                pizza.append(a)

    print('#{} {}'.format(tc, pizza[0][0]))
