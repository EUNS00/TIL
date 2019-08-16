N = int(input())
if 0<=N<=10000:
    for i in range(N):
        result = 0
        num = list(map(int, input().split()))
        for n in num:
            if n% 2:
                result += n
        print(f'#{i+1} {result}')

