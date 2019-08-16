N = int(input())

for tc in range(N):
    result = 0
    arr = list(map(int, input().split()))
    arr_re = sorted(arr)
    for num, i in enumerate(arr_re):
        if num==0 or num==(len(arr_re)-1):
            continue
        else:
            result += i
    
    print('#{} {}'.format(tc+1, round(result/(len(arr_re)-2)), 1))