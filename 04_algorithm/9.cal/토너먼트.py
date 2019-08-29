import sys
sys.stdin = open("토너먼트.txt")

T = int(input())

for tc in range(1, T+1):
    test = {}
    result = {}
    N = int(input())
    arr = list(map(int, input().split()))

    for num, a in enumerate(arr):
        test[num+1] = a

    count = 0

    while count != N:
        if len(test) >= 2:
            p1 = test.popitem()
            p2 = test.popitem()
            # print(p1, p2)
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
            # print(result, count)
            count += 1

        elif len(test) == 1:
            p1 = test.popitem()
            test = result
            result[p1[0]] = p1[1]
            # print(result, count)
            count += 1

        elif len(test) == 0:
            test = result
            count += 1

    for key in result.keys():
        print('#{} {}'.format(tc, key))
