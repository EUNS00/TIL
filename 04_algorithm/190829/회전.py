import sys
sys.stdin = open("회전.txt")

T = int(input())

for tc in range(1, T+1):
    N, ran = map(int, input().split())
    arr = list(map(int, input().split()))
    for i in range(ran):
        t = arr.pop(0)
        arr.append(t)
    print('#{} {}'.format(tc, arr[0]))