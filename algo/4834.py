import sys
sys.stdin = open("4834.txt")

for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input()))
    test = {}

    for _ in range(N):
        a = arr.pop()
        if a not in test:
            test[a] = 1
        else:
            test[a] += 1

    max_k, max_v = 0, 0
    for key, value in test.items():
        if max_k == 0 and max_v == 0:
            max_k, max_v = key, value
        else:
            if value > max_v:
                max_k, max_v = key, value
            elif value == max_v and key > max_k:
                max_k, max_v = key, value
    print('#{} {} {}'.format(tc, max_k, max_v))
