import sys
sys.stdin = open("view_input.txt")

for tc in range(10):
    result = 0
    N = int(input())
    arr = list(map(int, input().split()))
    
    for i in range(N):
        if i < 2:
            continue
        elif i == N-2:
            print('#{} {}' .format(tc+1, result))
            break
        else:
            miny = arr[i] - arr[i-2]
            sun = arr[i] - arr[i-1]
            if miny > sun:
                miny = sun
            sun = arr[i] - arr[i+1]
            if miny > sun:
                miny = sun
            sun = arr[i] - arr[i+2]
            if miny > sun:
                miny = sun
        if miny > 0:
            result += miny
