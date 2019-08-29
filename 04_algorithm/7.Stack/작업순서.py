import sys
sys.stdin = open("작업순서_input.txt")

for test_case in range(1, 11):
    v, e = map(int, input().split())
    arr = [[0] * (v + 1) for _ in range(v + 1)]

    Data = list(map(int, input().split()))
    N = int(len(Data) / 2)

    for i in range(N):
        x = Data[i * 2]
        y = Data[i * 2 + 1]
        arr[y][x] = 1
    result = []

    while True:
        if len(result) == v:
            break

        col = []
        for y in range(1, len(arr)):
            if 1 not in arr[y] and y not in result:
                col.append(y)

        for y in col:
            result.append(y)
            for x in range(len(arr)):
                arr[x][y] = 0

    print('#{}'.format(test_case), end=" ")
    for i in result:
        print(i, end=" ")
    print()