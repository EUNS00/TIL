import sys
sys.stdin = open("4835.txt")

for tc in range(1, int(input())+1):
    N, M = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    test = []
    for x in range(N-M+1):
        sum = 0
        for y in range(M):
            sum += arr[x+y]
        test.append(sum)
    test.sort()
    print('#{} {}'.format(tc, test[-1] - test[0]))