def DFS(start):
    global result
    visited[start] = 1
    for next in range(1, V+1):
        if arr[start][next] and not visited[next]:
            if next == end_node:
                result = 1
                return
            DFS(next)

import sys
sys.stdin = open("4871.txt")

for tc in range(1, int(input())+1):
    V, E = list(map(int, input().split()))

    arr = [[0 for _ in range(V+1)] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]
    for i in range(E):
        start, end = map(int, input().split())
        arr[start][end] = 1

    start_node, end_node = map(int, input().split())
    result = 0
    DFS(start_node)
    print('#{} {}'.format(tc, result))