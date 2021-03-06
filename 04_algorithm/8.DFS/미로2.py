def maze(y, x):
    global N, flag
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    visit[y][x] = 1
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny < 0 or ny == N: continue
        if nx < 0 or nx == N: continue
        if visit[ny][nx] == 1: continue
        if data[ny][nx] == 1: continue
        if data[ny][nx] ==3:
            flag= 1
            return
        maze(ny, nx)

def findStart(data):
    for y in range(N):
        for x in range(N):
            if data[y][x] == 2:
                return y, x

import sys
sys.stdin = open("미로.txt")

T = 10
N = 16
for tc in range(T):
    flag = 0
    no = int(input())

    data = [0 for _ in range(N)]
    for i in range(N):
        data[i] = list(input())
    visit = [[0 for _ in range(N)]for _ in range(N)]

    sy, sx = findStart(data)
    maze(sy, sx)
    print("#{} {}".format(tc + 1, flag))