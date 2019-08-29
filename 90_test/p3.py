import sys
sys.stdin = open("p3.txt")

wayx = [0, 0, 1, -1, 1, 1, -1, -1]
wayy = [1, -1, 0, 0, 1, -1, 1, -1]

def dfs(x, y):
    visited[x][y] = 1
    for z in range(8):
        if nxn[x+wayx[z]][y+wayy[z]] > 1 and visited[x+wayx[z]][y+wayy[z]] == 0:
            dfs(x+wayx[z], y+wayy[z])

def count(x, y):
    global cnt
    for z in range(8):
        if visited[x+wayx[z]][y+wayy[z]] == 1:
            return cnt
    cnt += 1
    return cnt

T = int(input())
if 1 <= T <= 10:
    for tc in range(1, T+1):
        N = int(input())

        arr = [list(map(int, input().split())) for _ in range(N)]
        nxn = [[0 for _ in range(N + 2)] for _ in range(N + 2)]
        visited = [[0 for _ in range(N + 2)] for _ in range(N + 2)]
        ans = []

        for i in range(1, N+1):
            for j in range(1, N+1):
                nxn[i][j] = arr[i-1][j-1]
        cnt = 0

        for i in range(1, N+1):
            for j in range(1, N+1):
                if nxn[i][j] >= 1 and visited[i][j] == 0:
                    dfs(i, j)
        c = 0

        for i in range(1, N+1):
            for j in range(1, N+1):
                if visited[i][j] == 1:
                    count(i, j)

        print('#{} {}'.format(tc, cnt))

