import sys
sys.stdin = open("p2.txt")

T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = [[0 for _ in range(N)] for _ in range(M)]

    for i in range(N):
        arr[i] = list(map(int, input().split()))

    result =0
    for x in range(N-K+1):
        for y in range(M-K+1):
            sum = 0
            for i in range(K):
                for j in range(K):
                    if (j == 0 or j == K-1) or (i == 0 or i == K-1):
                        sum += arr[x+i][y+j]
            if result <= sum:
                result = sum

    print('#{} {}'.format(tc, result))
