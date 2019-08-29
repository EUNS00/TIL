def Word(n):
    result = []
    for wl in range(len(n)):
        if n[wl] != n[wl - 1]:
            result.append(n[wl])
        elif result != []:
            if n[wl] == n[wl - 1]:
                result.pop()
    return len(result)

    # for w in range(len(n)):
    #     if w > 0:
    #         if n[w] == n[w - 1]:
    #             n = ''.join(result)
    #             print(len(n))
    #             return Word(n)


import sys
sys.stdin = open("반복문자_input.txt")

T = int(input())
for tc in range(1, T + 1):
    word = input()
    print(Word(word))


