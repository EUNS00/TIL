import sys
sys.stdin = open("회문_2input.txt")

T = int(input())

for test_case in range(1, T+1):
    N, M = list(map(int, input().split()))

    arr = [[0 for _ in range(N)] for _ in range(N)]
    for x in range(N):
        word = input()
        for num, i in enumerate(word):
            arr[x][num] = i

    for x in range(len(arr)):
        for y in range(len(arr[x])):
            if N-M >= y:
                cnt = 0
                result = []
                while cnt != M:
                    result += arr[x][y+cnt]
                    cnt += 1
                Word = ''.join(result)
                if Word == Word[::-1]:
                    pal = Word

    for x in range(len(arr)):
        for y in range(len(arr[x])):
            if N-M >= y:
                cnt = 0
                result = []
                while cnt != M:
                    result += arr[y+cnt][x]
                    cnt += 1
                Word = ''.join(result)
                if Word == Word[::-1]:
                    pal = Word

    print('#{} {}'.format(test_case, pal))