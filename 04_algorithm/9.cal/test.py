import sys
sys.stdin = open("토너먼트.txt")

T = int(input())

for tc in range(1, T + 1):
    test = {}
    result = {}
    N = int(input())
    arr = list(map(int, input().split()))

    for num, a in enumerate(arr):
        test[num + 1] = a
    cnt = 0
    p3 = 0
    while cnt != N-1:
        if len(test) % 2 == 1:
            p3 = test.popitem()

        elif len(test) == 0:
            for i in range(len(result)):
                retu = result.popitem()
                test[retu[0]] = retu[1]
            if p3 != 0:
                test[p3[0]] = p3[1]

        else:
            p1 = test.popitem()
            p2 = test.popitem()
            if p1[1] == 1:
                if p2[1] == 2:
                    result[p2[0]] = p2[1]
                elif p2[1] == 3:
                    result[p1[0]] = p1[1]
                elif p2[1] == 1:
                    result[p1[0]] = p1[1]
            elif p1[1] == 2:
                if p2[1] == 3:
                    result[p2[0]] = p2[1]
                elif p2[1] == 1:
                    result[p1[0]] = p1[1]
                elif p2[1] == 2:
                    result[p1[0]] = p1[1]
            elif p1[1] == 3:
                if p2[1] == 1:
                    result[p2[0]] = p2[1]
                elif p2[1] == 2:
                    result[p1[0]] = p1[1]
                elif p2[1] == 3:
                    result[p1[0]] = p1[1]
            print('result : {}'.format(result))
            cnt += 1

    for i in result.keys():
        print('#{} {}'.format(tc, i))