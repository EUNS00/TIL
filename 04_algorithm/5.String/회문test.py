import sys
sys.stdin = open("회문.txt")

for test_case in range(1, 11):
    test_num = int(input())
    arr = [[0 for _ in range(100)] for _ in range(100)]
    for x in range(100):
        word = input()
        for num, i in enumerate(word):
            arr[x][num] = i

    for x in range(len(arr)):

        for c in range(100):
            res = []
            res2 = []

            for y in range(c, len(arr[x])):
                res += arr[x][y]
                res2 += arr[y][x]
                res = ''.join(res)
                res2 = ''.join(res2)

                if x == 0 and y == 0:
                    data = res

                elif res == res[::-1] or res2 == res2[::-1]:
                    if len(res) > len(data) or len(res2) > len(data):
                        if len(data) <= len(res):
                            data = res
                        if len(data) <= len(res2):
                            data = res2

    print('#{} {}'.format(test_case, len(data)))