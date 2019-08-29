import sys
sys.stdin = open("Forth.txt")

T = int(input())
for tc in range(1, T+1):
    num = []
    cal = []
    a = 0
    word = list(map(str, input().split()))
    for w in word:
        if w == '+' or w == '*' or w == '-' or w == '/' or w == '.':
            cal.append(w)
        else:
            num.append(int(w))

    while cal != []:
        a = cal.pop(0)
        if a == '.':
            break
        elif len(num) >= 2 :
            num1 = num.pop(0)
            num2 = num.pop(0)
        if a == '+':
            num3 = num1 + num2
        elif a == '-':
            num3 = num1 - num2
        elif a == '*':
            num3 = num1 * num2
        elif a == '/':
            num3 = num1 / num2
        num.append(num3)
    for i in num:
        print('#{} {}'.format(tc, i))
        break
