def bfs(v):
    queue.append(v)
    visited[v] = 1
    print(v, end=" ")
    while len(queue) != 0:
        v = queue.pop(0)
        for w in range(1, N+1):
            if arr[v][w] == 1 and visited[w] == 0:
                queue.append(w)
                visited[w] = visited[v] + 1
                print(w, end=" ")

import sys
sys.stdin = open("BFS.txt")

N, M = map(int, input().split())
temp = list(map(int, input().split()))

queue = []
arr = [[0 for _ in range(N+1)] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for i in range(0, len(temp), 2):
    arr[temp[i]][temp[i+1]] = 1
    arr[temp[i+1]][temp[i]] = 1

for i in range(N+1):
    print('{} {}'.format(i, arr[i]))

bfs(1)
print()
