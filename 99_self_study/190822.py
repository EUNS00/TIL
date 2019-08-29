def Route(s):
    global L, result, e
    if s == e:
        result = 1
        return
    for i in range(len(L)):
        if L[i][0] == s:
            z = L[i]
            L[i] = 'a'
            Route(z[1])

import sys
sys.stdin = open("그래프경로_input.txt")

T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    result = 0
    L = [input().replace(' ', '') for i in range(E)]
    s, e = map(str, input().split())
    Route(s)
    print(tc, result)