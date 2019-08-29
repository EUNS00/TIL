import sys
sys.stdin = open("2001_input.txt")

T = int(input())
for test_case in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr = [[0 for _ in range(N)] for _ in range(N)]
    for L in range(N):
        l = list(map(int, input().split()))
        arr[L] = l
    print(arr)

    for x in range(len(arr)):
        for y in range(len(arr[x])):
            count = 0
            result = 0
            if y >= M - 1 and x >= M - 1:
                while count != M**2:
                    if result == 0:
                        result += arr[x][y]
                    # elif :
                    # count += 1
            print('x:{}, y:{}, {}'.format(x, y, arr[x][y]))

# while len(result) != N:
#     result += arr[x][y - num]
#     num += 1
# pal = ''.join(result)