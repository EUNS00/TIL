def ispass(y, x):
    if 0 <= y < N and 0 <= x < N and arr[y][x] != 1 and visited[y][x] == 0:
        return True
    else:
        return False


def DFS(sy, sx):
    global end
    visited[sy][sx] = 1
    if arr[sy][sx] == 3:
        end = 1

    for i in range(4):
        ny = sy + dy[i]
        nx = sx + dx[i]
        if ispass(ny, nx):
            visited[ny][nx] = 1
            DFS(ny, nx)

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


import sys
sys.stdin = open("미로.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                start = (i, j)
    end = 0

    DFS(start[0], start[1])

    print('#{} {}'.format(tc, end))
