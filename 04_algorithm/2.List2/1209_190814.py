import sys
sys.stdin = open("1209_input.txt")
for i in range(10):
    N = int(input())
    arr = [[0 for _ in range(100)] for _ in range(100)]
    for i in range(100):
        arr[i] = list(map(int, input().split()))

    Max = 0
    Max_x = -10
    Max_y = -10

    sum_y = []
    sum_xy = 0
    sum_rxy = 0
    for x in range(len(arr)):
        sum_x = 0
        for y in range(len(arr[x])):
            sum_x += arr[x][y]
            if x==y:
                sum_xy += arr[x][y]
            if y==99:
                sum_rxy += arr[x][99-x]
            if sum_y == []:
                sum_y = arr[x]
            elif x > 0:
                sum_y[y] += arr[x][y]
        if Max_x<sum_x:
            Max_x = sum_x
    for i in sum_y:
        if i > Max_y:
            Max_y = i

    if Max < sum_xy:
        Max = sum_xy
    if Max < sum_rxy:
        Max = sum_rxy
    if Max < Max_x:
        Max = Max_x
    if Max < Max_y:
        Max = Max_y

    print('#{} {}'.format(N, Max))