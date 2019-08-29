def solve(arr):
    global N
    X, Y = 0, 0
    newX, newY = 0, 0
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]


    dir_stat = 0
    num = 1
    for i in range(N*N):
        X, Y = newX, newY
        arr[Y][X] = num
        newX = X + dx[dir_stat]
        newY = Y + dy[dir_stat]

        if newY >= N or newX >= N or newY < 0 or newX < 0 or arr[newY][newX] != 0:
            dir_stat = (dir_stat + 1) % 4
            newX = X + dx[dir_stat]
            newY = Y + dy[dir_stat]

        num += 1

import sys
sys.stdin = open("달팽이.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [[0 for _ in range(N)] for _ in range(N)]

    solve(arr)

    print('#{} {}'.format(tc, arr))