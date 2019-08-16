import sys
sys.stdin = open("list_06.txt")
T = int(input())
if 1 <= T <= 50:
    for test_case in range(1, T+1):
        Min = 19191910
        Max = -19191910
        result = 0
        N = int(input())
        if 5 <= N <= 1000:
            ai = list(map(int, input().split()))
            for i in ai:
                if i > Max:
                    Max = i
                elif i < Min:
                    Min = i
            print('#{} {}'.format(test_case, Max-Min))