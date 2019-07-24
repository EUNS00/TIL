N = int(input())
if 1<=N<=10:
    for number in range(N):
        print(f'#{number+1}', end=' ')
        math = int(input())
        msum = 0
        for m in range(math):
            if m%2:
                msum = msum - (m+1)
            else:
                msum = msum + (m+1)
        print(f'{msum}')
