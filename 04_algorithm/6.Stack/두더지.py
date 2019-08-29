import sys
sys.stdin = open("두더지.txt")

wayx = [0,0,1,-1]
wayy = [1,-1,0,0]
def dfs(x, y, cnt):
    visited[x][y] = cnt
    for z in range(4):
        if nxn[x+wayx[z]][y+wayy[z]] == 1 and visited[x+wayx[z]][y+wayy[z]] == 0:
            dfs(x+wayx[z], y+wayy[z], cnt)

N = int(input())
nxn = [[0 for _ in range(N+2)] for _ in range(N+2)]
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(N+2)] for _ in range(N+2)]
ans = []

for i in range(1, N+1):
    for j in range(1, N+1):
        nxn[i][j] = arr[i-1][j-1]
cnt = 0

for i in range(1, N+1):
    for j in range(1, N+1):
        if nxn[i][j] == 1:
            if visited[i][j] == 0:
                cnt += 1
                dfs(i, j, cnt)
c = 0

for n in range(1, cnt+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if visited[i][j] == n:
                c += 1
                ans.append(c)
c = 0

ans.sort(reverse=True)
print(cnt)
for i in range(len(ans)):
    print(ans[i])