T = int(input())
if 0<=T<=10000:
    for i in range(T):
        result = 0
        num = list(map(int, input().split()))
        for n in num:
            result += n
        result = round(result/len(num))
        print(f'#{i+1} {result}')
