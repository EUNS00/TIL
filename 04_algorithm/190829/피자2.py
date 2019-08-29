import sys
sys.stdin = open("피자.txt")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    Q = []
    for i in range(N):
        Q.append([arr[i], i])

    i = 0
    while len(Q)!=1:
        Q[0][0] //= 2

        if Q[0][0] == 0:
            if N+ i < M:
                Q.pop(0)
                Q.append([arr[N+i], N+i])
                i+=1
            elif N+i >= M:
                Q.pop(0)
        else:
            Q.append(Q.pop(0))
        print(Q)

    print('#{} {}'.format(tc, Q[0][1]+1))