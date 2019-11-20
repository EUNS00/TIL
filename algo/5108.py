import sys
sys.stdin = open("5108.txt")

for tc in range(1, int(input())+1):
    N, M, L = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    for i in range(M):
        test = list(map(int, input().split()))
        arr.insert(test[0], test[1])

    print('#{} {}'.format(tc, arr[L]))