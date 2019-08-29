import sys
sys.stdin = open("파리.txt")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for x in range(N-M+1):
        for y in range(N-M+1):
            Sum = 0
            for i in range(M):
                for j in range(M):
                    Sum += arr[x+i][y+j]
                    result = max(Sum, result)
    print('#{} {}'.format(tc, result))

