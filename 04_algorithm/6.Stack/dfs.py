def dfs(n):
    visited[n] = 1
    print(n, end=" ")

    for w in range(V+1):
        if G[n][w] == 1 and visited[w] == 0:
            dfs(w)

import sys
sys.stdin = open("dfs.txt")

V, E = map(int, input().split())
temp = list(map(int, input().split()))

G = [[0 for i in range(V+1)] for j in range(V+1)]
visited = [0 for i in range(V+1)]

for i in range(0, len(temp), 2):
    G[temp[i]][temp[i+1]] = 1
    G[temp[i+1]][temp[i]] = 1

# for i in range(n+1):
#     print("{} {}".format((i, G[i])))

dfs(1)