import sys
sys.stdin = open("그래프경로_input.txt")

T = int(input())

for tc in range(1, T+1):
    cnt = 0
    V, E = map(int, input().split())

    if V > E:
        temp = [[0 for _ in range(V+1)] for _ in range(V+1)]
        visited = [[0 for _ in range(V+1)] for _ in range(V+1)]
    else:
        temp = [[0 for _ in range(E+1)] for _ in range(E+1)]
        visited = [[0 for _ in range(E + 1)] for _ in range(E + 1)]

    for e in range(E):
        S, G = map(int, input().split())
        for x in range(len(temp)):
            for y in range(len(temp[x])):
                if x == S and y == G:
                    temp[x][y] = 1
                    temp[y][x] = 1
                elif x == G and y == S:
                    temp[x][y] = 1
                    temp[y][x] = 1

    for x in range(len(temp)):
        for y in range(len(temp[x])):
            if temp[x][y]==1 and x == S and y == G and visited[x][y] == 0 and cnt == 0:
                visited[x][y] = 1
                visited[y][x] = 1
                cnt += 1
            # if temp[x][y]==1 and

    print(temp)
    print(visited)
