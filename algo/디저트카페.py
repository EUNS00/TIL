import sys
sys.stdin = open("디저트카페.txt")

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    test = []
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            if 0 < x < N-1 and 0 < y < N-1:
                test.append([x, y])

    print(test)
    test2 = []
    for i in test:
        if [i[0] + 1, i[1] + 1] in test:
            test2.append([[i[0], i[1]], [i[0]+1, i[1]+1]])
        elif [i[0] - 1, i[1] + 1] in test:
            test2.append([[i[0], i[1]], [i[0] - 1, i[1] + 1]])
    print(test2)