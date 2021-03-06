import sys
sys.stdin = open("Forth.txt")

def find():
    s = []
    for i in range(len(code)):
        if code[i] == '+' or code[i] == '-' or code[i] == '/' or code[i] == '*':  #연산자
            if len(s) >= 2:
                op2 = int(s.pop())
                op1 = int(s.pop())
                if code[i] == '+':
                    s.append(op1 + op2)
                elif code[i] == '-':
                    s.append(op1 - op2)
                elif code[i] == '*':
                    s.append(op1 * op2)
                elif code[i] == '/':
                    s.append(op1 // op2)
            else:
                return 'error'
        elif code[i] != ' ' and code[i] != '.':  #피연산자
            s.append(code[i])
        elif code[i] == '.':
            if len(s) == 1:
                return s.pop()
            else:
                return 'error'



T = int(input())

for tc in range(1, T + 1):
    code = list(input().split())

    print('#{} {}'.format(tc, find()))
