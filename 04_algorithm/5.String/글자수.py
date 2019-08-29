import sys
sys.stdin = open("글자수_input.txt")

T = int(input())

for test_case in range(1, T+1):
    result = {}
    str1 = input()
    str2 = input()

    Max = 0
    for st1 in str1:
        cnt = 0
        for st2 in str2:
            if st1 == st2:
                cnt += 1
            if Max < cnt:
                Max = cnt

    print('#{} {}'.format(test_case, Max))