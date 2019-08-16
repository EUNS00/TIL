import sys
sys.stdin = open("list_07.txt")
T = int(input())
if 1 <= T <= 50:
    for test_case in range(1, T + 1):
        K, N, M = map(int, input().split())
        b = list(map(int, input().split()))
        b.insert(0,0)
        b.append(N)

        for num, i in enumerate(b):
            count = 0
            posision = 0
            if b[num]- b[num-1] > K:
                count = 0
                break
            if b[i] > posision + K:
                posision = b[i-1]
                count += 1
        print('#{} {} {}'.format(test_case, count, posision))