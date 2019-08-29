import sys
sys.stdin = open("4861.txt")

T = int(input())

for test_case in range(1, T+1):
    N, M = list(map(int, input().split()))

    arr = [[0 for _ in range(N)] for _ in range(N)]
    for x in range(N):
        word = input()
        for num, i in enumerate(word):
            arr[x][num] = i

    if N == M :
        for x in range(len(arr)):
            result = []
            for y in range(len(arr[x])):
                result += arr[x][y]
            Word = ''.join(result)
            if Word == Word[::-1]:
                pal = Word

            result = []
            for y in range(len(arr[x])):
                result += arr[y][x]
            Word = ''.join(result)
            if Word == Word[::-1]:
                pal = Word

    print('#{} {}'.format(test_case, pal))