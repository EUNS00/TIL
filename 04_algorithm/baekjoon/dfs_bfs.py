def dfs(n):
    visited[n] = 1
    print(n, end=" ")

    for w in range(V+1):
        if G[n][w] == 1 and visited[w] == 0:
            dfs(w)

import sys
sys.stdin = open("dfs_bfs.txt")

N, M, V = map(int, input().split())
temp = []

for route in range(M):
    C, D = map(int, input().split())
    temp += C, D

G = [[0 for i in range(N+1)] for j in range(N+1)]
visited = [0 for i in range(N+1)]

for i in range(0, len(temp), 2):
    G[temp[i]][temp[i+1]] = 1
    G[temp[i+1]][temp[i]] = 1
print(visited)
dfs(N)