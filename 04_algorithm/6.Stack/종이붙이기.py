def paper(x):
    if x == N:
        return 1
    if x > N:
        return 0
    return paper(x+10) + paper(x+20) * 2

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    print('#{} {}'.format(tc, paper(0)))

    #f(n)=f(n-1)+2*f(n-2)