import sys
sys.stdin = open("190813.txt")

for test_case in range(1, 11):
    N = int(input())
    num = list(map(int, input().split()))
    for i in range(N):
        Max = 0
        Min = 100
        max_ind = 0
        min_ind = 0
        for comp_index in range(100):
            if num[comp_index] > Max:
                Max = num[comp_index]
                max_ind = comp_index
            if num[comp_index] < Min:
                Min = num[comp_index]
                min_ind = comp_index
        num[max_ind] -= 1
        num[min_ind] += 1
    Max = 0
    Min = 100
    for comp_index in range(100):
        if num[comp_index] > Max:
            Max = num[comp_index]
        if num[comp_index] < Min:
            Min = num[comp_index]
    print('#{} {}' .format(test_case, Max - Min))