def bfs(sy, sx):
    global end
    queue.append(sy)
    queue.append(sx)
    visited[sy][sx] = 1

    # if arr[sy][sx] == 3:
    #     end = visited[sy][sx]

    while len(queue) != 0:
        sy = queue.pop(0)
        sx = queue.pop(0)
        print(arr[sy][sx], end=" ")
        for i in range(4):
            ny = sy + dy[i]
            nx = sx + dx[i]
            if 0 <= ny < N and 0 <= nx < N and arr[ny][nx] != 1 and visited[sy][sx] == 0:
                queue.append(ny)
                queue.append(nx)
                visited[ny][nx] = 1
                print(arr[ny][nx], end=" ")


import sys
sys.stdin = open("미로.txt")
#
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
queue = []

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                start = (i, j)

    end = 0

    bfs(start[0], start[1])

    print(arr)
    print(visited)