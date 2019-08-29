def Word(n):
    result = []
    for wl in range(len(n)):
        if not result or result[-1] != n[wl]:
            result.append(n[wl])
        elif result and result[-1] == n[wl]:
            result.pop()
    return len(result)

import sys
sys.stdin = open("반복문자_input.txt")

T = int(input())

for tc in range(1, T + 1):
    word = input()
    print('#{} {}'.format(tc, Word(word)))