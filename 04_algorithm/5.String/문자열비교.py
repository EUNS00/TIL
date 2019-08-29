import sys
sys.stdin = open("문자열비교_input.txt")

T = int(input())
for test_case in range(1, T+1):
    T1 = input()
    T2 = input()
    lenT = len(T1)
    status = 0

    for num, i in enumerate(T2):
        result = []
        cnt = 0
        if num >= lenT-1:
            while cnt != lenT:
                result += T2[num-cnt]
                cnt += 1
            result = ''.join(result)
            if T1 == result[::-1]:
                status = 1

    print('#{} {}'.format(test_case, status))
