num_1 = int(input())
num_2 = 0
num_3 = 1
eq = ''

for i_1 in range(num_1):
    a,b = map(int,input().split())
    if a>b:
        eq = '>'
    elif a==b:
        eq = '='
    else:
        eq = '<'
    print(f'#{num_3} {eq}')
    num_3 += 1