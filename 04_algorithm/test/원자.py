def bigbang(a):
    global cnt
    for i in range(len(arr)):
        test = arr[i]
        for j in range(i, len(arr)):
            if test[0] == arr[j][0] or test[0] == arr[j][0]*-1:
                    arr.pop(i)
                    arr.pop(j-1)
                    cnt += test[3]
                    cnt += arr[j][3]
                    print(arr, cnt)
                    return bigbang(N-2)


import sys
sys.stdin = open("원자.txt")

T = int(input())
for tc in range(1):
    N = int(input())
    cnt = 0
    arr = [list(map(int, input().split())) for _ in range(N)]

    bigbang(N)