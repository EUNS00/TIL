import sys
sys.stdin = open("회문_0112.txt")

for test_case in range(1):
    test_num = int(input())
    arr = [[0 for _ in range(10)] for _ in range(10)]
    for x in range(10):
        word = input()
        for num, i in enumerate(word):
            arr[x][num] = i
    num = 0
    cnt = 0
    for x in range(len(arr)):
        result = []
        for y in range(len(arr[x])):
            while cnt <= num:
                result += arr[x][y]
                cnt += 1
                result = ''.join(result)
                if result == result[::-1]:
                    if x==0 and y==0:
                        word = result
                    elif len(word) <= len(result):
                        word = result
            num += 1

        # for y in range(len(arr[x])):
        #     print(cnt, num, x)
        #     while cnt <= num:
        #         result += arr[y][x]
        #         cnt += 1
        #         result = ''.join(result)
        #         if result == result[::-1]:
        #             word = result
        #     num += 1

        print(word)




