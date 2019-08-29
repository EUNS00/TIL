import sys
sys.stdin = open("1979.txt")

T = int(input())

for test_case in range(1, T+1):
    N, K = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    for x in range(len(arr)):
        result = []
        result2 = []
        for y in range(len(arr[x])):
            result.append(arr[x][y])
            result2.append(arr[y][x])
        print(result, result2, K)
    print()