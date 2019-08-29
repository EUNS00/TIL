import sys
sys.stdin = open("평균값.txt")

T = int(input())

for tc in range(1, T+1):
    result = 0
    temp = list(map(int, input().split()))
    temp.sort()
    for num, val in enumerate(temp):
        if num == 0 or num == len(temp)-1:
            continue
        else:
            result += val
    value = round(result / (len(temp) - 2), 0)

    print('#{} {}'.format(tc, int(value)))