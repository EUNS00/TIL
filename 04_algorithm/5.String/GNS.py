import sys
sys.stdin = open("GNS.txt")

Num_word = ("ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN")
T = int(input())
for test_case in range(1, T+1):
    test_box = {}
    Num_box = {}
    test, N = list(map(str, input().split()))
    case = int(N)
    if 100 <= case <= 10000:
        day = list(map(str, input().split()))

        for num, n in enumerate(Num_word):
            Num_box[num] = n

        for d in day:
            if d not in test_box:
                test_box[d] = 1
            else:
                test_box[d] += 1

        for num, value_n in enumerate(Num_box.values()):
            for key, value in test_box.items():
                if value_n == key:
                    Num_box[num] = key, value
        print('#{}'.format(test_case))

        for value in Num_box.values():
            cnt = 1
            while cnt <= value[1]:
                print(value[0], end=" ")
                cnt += 1
        print()