import sys
sys.stdin = open("1204.txt")

for tc in range(1, int(input())+1):
    TC = int(input())
    arr = list(map(int, input().split()))
    test = {}
    for a in arr:
        if a not in test:
            test[a] = 1
        else:
            test[a] += 1

    a = []
    for key, value in test.items():
        if a == []:
            a = [key, value]
        elif a[1] < value:
            a = [key, value]

    print('#{} {}'.format(tc, a[0]))