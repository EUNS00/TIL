def count():
    global ans
    sum = 0
    for i in range(N):
        for j in range(M):
            if copied[i][j] == 0: sum += 1
    if ans < sum: ans = sum

def copyArr():
    # 바이러스가 번진 지도를 위해 복사함
    for i in range(N):
        for j in range(M):
            copied[i][j] = arr[i][j]

def bfs():
    deq = collections.deque()
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    copyArr()
    # 바이러스 좌표를 인큐
    for i in range(N):
        for j in range(M):
            if copied[i][j] == 2:
                deq.append((i,j))

    # 바이러스 번지게 함
    while deq:
        x, y = deq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N :continue
            if ny < 0 or ny >= M : continue
            if copied[nx][ny] == 1 : continue
            if copied[nx][ny] == 0 : # 빈칸
                copied[nx][ny] = 2
                deq.append((nx, ny))
    count()

# 벽 세우기
def dfs(cnt):
    if cnt == 3:
        bfs()
        return
    else:
        for i in range(N):
            for j in range(M):
                if arr[i][j] == 0: #벽세우기
                    arr[i][j] = 1
                    dfs(cnt + 1)
                    arr[i][j] = 0

import collections
ans = 0
import sys
sys.stdin = open("연구소.txt")

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())  # 3 ≤ N(세로), M(가로) ≤ 8
    arr = [list(map(int, input().split())) for _ in range(N)]
    copied = [[0 for _ in range(M)] for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                arr[i][j] = 1
                dfs(1)
                arr[i][j] = 0

    print(ans)