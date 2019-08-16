import sys
sys.stdin = open("색칠하기_input.txt")

N = int(input())
for i in range(1, N+1):
    arr = [[0 for _ in range(10)] for _ in range(10)]
    n = int(input())
    for j in range(n):

        p1_x = 0
        pl_y = 0
        p2_x = 0
        p2_y = 0
        color = 0
        co_count = 0
        l = list(map(int, input().split()))
        for num, q in enumerate(l):
            if num == 0:
                p1_x = q
            elif num == 1:
                p1_y = q
            elif num == 2:
                p2_x = q
            elif num == 3:
                p2_y = q
            elif num == 4:
                color = q

        # print(p1_x, p1_y, p2_x, p2_y, color)

        for x in range(len(arr)):
            for y in range(len(arr[x])):
                if p1_x<=x<=p2_x and p1_y<=y<=p2_y and color==0:
                    arr[x][y] = color
                elif p1_x<=x<=p2_x and p1_y<=y<=p2_y and color!=0:
                    arr[x][y] += color
        # print(arr)

    for x in range(len(arr)):
        for y in range(len(arr[x])):
            if arr[x][y]==3:
                co_count+=1
    print('#{} {}'.format(i, co_count))