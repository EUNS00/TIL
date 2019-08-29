
import sys
sys.stdin = open("괄호검사_input.txt")

T = int(input())

if 1 <= T <= 50:
    for tc in range(1, T+1):
        word = input()
        N = len(word)
        result = []
        for w in range(N):
            if word[w] == "(" or word[w] == "{":
                result.append(word[w])

            elif word[w] == ")" or word[w] == "}":
                if result == []:
                    result = word[w]
                    break
                elif (word[w] == ")" and result[-1] != "(") or (word[w] == "}" and result[-1] != "{"):
                    result = word[w]
                    break
                else:
                    result.pop()

        if len(result) != 0:
            stack = 0
        else:
            stack = 1

        print('#{} {}'.format(tc, stack))