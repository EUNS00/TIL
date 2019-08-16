import sys
sys.stdin = open("list_09.txt")
T = int(input())
if 1 <= T <= 50:
    for test_case in range(1, T + 1):
        Max = 0
        Min = 0
        result = {}
        N = list(map(int, input().split()))
        a = list(map(int, input().split()))
        for num, i in enumerate(N):
            if num == 0:
                Number = i
            elif num == 1:
                count = i

        for num2, i2 in enumerate(a):
            Sum = 0
            if num2 >= i-1:
                for num3 in range(i):
                    Sum += a[num2 - num3]
                if num2 == i-1:
                    Max = Sum
                    Min = Sum
                else:
                    if Max < Sum:
                        Max = Sum
                    elif Min > Sum:
                        Min = Sum
        print('#{} {}'.format(test_case, Max-Min))