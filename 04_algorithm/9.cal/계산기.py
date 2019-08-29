
import sys
sys.stdin = open("계산기.txt")

for tc in range(1):
    N = int(input())
    word = input()
    test = []
    result = []
    cal = []

    for w in word:
        if w == '(' or w == '*' or w == '+':
            test.append(w)
        elif w == ')':
            while test != []:
                a = test.pop()
                if a == '(':
                    break
                num1 = result.pop()
                num2 = result.pop()
                if a == '+':
                    num3 = num1 + num2
                result.append(num3)
        else:
            result.append(int(w))

        if w == '+':
            test.pop()
            while test != []:
                a = test.pop()
                if a == '(':
                    test.append('+')
                    break
                num1 = result.pop()
                num2 = result.pop()
                if a == '*':
                    num3 = num1 * num2
                    result.append(num3)




        print('test : {}'.format(test))
        print('result : {}'.format(result))
