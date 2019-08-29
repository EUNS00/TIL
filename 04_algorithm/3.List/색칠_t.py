import sys
sys.stdin = open("색칠하기_input.txt")
T = int(input())
N = 10
for test_case in range(1, N+1):
    data = [[0] * N for i in range(N)]

    n = int(input())
    cnt = 0

    for k in range(n):
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                data[i][j] += color

    for i in range(N):
        for j in range(N):
            if(data[i][j] == 3): cnt += 1

    print("#{} {}".format(test_case, cnt))