import sys
sys.stdin = open("list_08.txt")
T = int(input())
if 1 <= T <= 50:
    for test_case in range(1, T + 1):
        result = {}
        N = int(input())
        a = input()
        if len(a) == \
                N:
            for i in a:
                if i not in result:
                    num = 1
                    result[i] = num
                else:
                    result[i] += 1
        for num, (key, value) in enumerate(result.items()):
            if num == 0:
                Max_k, Max_v = key, value
            else:
                if value > Max_v:
                    Max_k, Max_v = key, value
                elif value == Max_v and int(Max_k) < int(key):
                    Max_k, Max_v = key, value

        print('#{} {} {}'.format(test_case,Max_k, Max_v))