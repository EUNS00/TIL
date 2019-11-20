import sys
sys.stdin = open("4836.txt")

for tc in range(1, int(input())+1):
    number = int(input())
    arr = [[0 for _ in range(10)] for _ in range(10)]

    for _ in range(number):
        color = list(map(int, input().split()))
        for x in range(10):
            for y in range(10):
                if color[0] <= x <= color[2] and color[1] <= y <= color[3]:
                    arr[x][y] += color[4]
    test = {}
    for x in range(10):
        for y in range(10):
            if arr[x][y] not in test:
                test[arr[x][y]] = 1
            else:
                test[arr[x][y]] += 1

    print('#{} {}'.format(tc, test[3]))