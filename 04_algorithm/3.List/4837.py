import sys
sys.stdin = open("부분집합_input.txt")

T = int(input())
for i in range(1, T+1):
    result = 0
    N, K = list(map(int, input().split()))
    if 1 <= N <= 12 and 1 <= K <= 100:
        for n in range(1, 13):
            Sum = 0
            cnt = 0
            if n > N-1:
                for z in range(N):
                    Sum += n-cnt
                    cnt += 1

            if Sum == K:
                result += 1
    print('#{} {}'.format(i, result))

