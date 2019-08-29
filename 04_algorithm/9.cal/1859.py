T = int(input())

for tc in range(1, T+1):
    N = int(input())
    M = list(map(int, input().split()))
    Max = 0

    for num, m in enumerate(M):
        if num == 0:
            Max = m
        elif Max < m:
            Max = m
    if Max <= M[0]:
        print(0)
    else:
        Sum = 0
        for i in M:
            Sum += Max-i
        print(Sum)