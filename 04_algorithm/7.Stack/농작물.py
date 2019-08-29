import sys
sys.stdin = open("농작물.txt")

T = int(input())

for tc in range(1, T+1):

    N = int(input())
    arr = [list(map(int, input())) for i in range(N)]

    Sum = 0
    mid = N // 2
    start = mid
    end = mid
    for i in range(N):

        for j in range(start, end+1, 1):
            Sum += arr[i][j]

        if i < mid:
            start -= 1
            end += 1

        else:
            start += 1
            end -= 1
    print('#{} {}'.format(tc, Sum))