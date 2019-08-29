import sys
sys.stdin = open("test.txt")

T = int(input())

for tc in range(1, T+1):
    Max = 0
    N, M, K = map(int, input().split())
    arr = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(K):
        test = 0
        word = list(map(int, input().split()))
        if 5 <= N <= 100 and 5 <= M <= 100 and 1 <= K <= 20:
            if 0 <= word[4] <= 10:
                if 0 <= word[0] <= N-1 and 0 <= word[2] <= N-1 and 0 <= word[1] <= M-1 and 0 <= word[3] <= M-1:
                    if Max <= word[4]:
                        Max = word[4]

                    for x in range(len(arr)):
                        for y in range(len(arr[x])):
                            if word[0] <= x <= word[2] and word[1] <= y <= word[3]:
                                if arr[x][y] > word[4]:
                                    test = 1

                    for x in range(len(arr)):
                        for y in range(len(arr[x])):
                            if word[0] <= x <= word[2] and word[1] <= y <= word[3] and test == 0:
                                arr[x][y] = word[4]
        else:
            break

    cnt_max = []
    for i in range(Max+1):
        cnt = 0
        for x in range(len(arr)):
            for y in range(len(arr[x])):
                if arr[x][y] == i:
                    cnt += 1

        if cnt_max == []:
            cnt_max = i, cnt
        elif cnt_max[1] < cnt:
            cnt_max = i, cnt
    print('#{} {}'.format(tc, cnt_max[1]))
