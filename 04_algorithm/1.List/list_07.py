import sys
sys.stdin = open("list_07.txt")
T = int(input())
if 1 <= T <= 50:
    for test_case in range(1, T + 1):
        count = 0
        posision = 0
        a = list(map(int, input().split()))
        for num, i in enumerate(a):
            if num == 0:
                K = i
            elif num == 1:
                N = i
            else:
                M = i
        b = list(map(int, input().split()))

        for num2, i2 in enumerate(b):
            if num2 < len(b):
                if posision % K != 0:
                    if posision + K == N:
                        continue
                    posision = i2
                    count += 1
                elif posision % K == 0:
                    posision = i2
                    count += 1
            if b[num2]-b[num2-1] > K:
                count = 0
                break
            print('#{} {} {}'.format(test_case, count, posision))