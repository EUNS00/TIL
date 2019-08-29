import sys
sys.stdin = open("p1.txt")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0 for _ in range(N)] for _ in range(N)]
    for case in range(M):
        x1, y1, x2, y2 = map(int, input().split())

        for x in range(len(arr)):
            for y in range(len(arr[x])):
                if x1 <= x <= x2 and y1 <= y <= y2:
                    arr[x][y] = 1

    count = 0
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            if arr[x][y] == 1:
                count += 1
    print('#{} {}'.format(tc, count))

