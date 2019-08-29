def solve(arr):
    global N
    X, Y = 0, 0
    newX, newY = 0, 0
    dx = [1, 0, -1, 0] # 우하좌상
    dy = [0, 1, 0, -1]
    dir_start = 0

    for i in range(1, N*N+1):
        X, Y = newX, newY
        arr[Y][X] = i
        newX = X + dx[dir_start]
        newY = Y + dy[dir_start]

        if newY >= N or newX >= N or newY < 0 or newX < 0 or arr[newY][newX] != 0:
            dir_start = (dir_start + 1) % 4
            newX = X + dx[dir_start]
            newY = Y + dy[dir_start]


# import sys
# sys.stdin = open("달팽이.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [[0 for _ in range(N)] for _ in range(N)]

    solve(arr)

    print('#{}'.format(tc))
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            print(arr[x][y], end=" ")
        print()
