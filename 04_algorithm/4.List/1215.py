import sys
sys.stdin = open("1215.txt")

for test_case in range(1, 11):
    N = int(input())
    arr = [[0 for _ in range(8)] for _ in range(8)]

    for L in range(8):
        word = input()
        for num, i in enumerate(word):
            arr[L][num] = i
    count = 0

    for x in range(len(arr)):
        for y in range(len(arr[x])):
            result = []
            num = 0
            if y >= N - 1:
                while len(result) != N:
                    result += arr[x][y-num]
                    num += 1
                pal = ''.join(result)
                if pal == pal[::-1]:
                    count+=1

    for x in range(len(arr)):
        for y in range(len(arr[x])):
            result = []
            num = 0
            if x >= N - 1:
                while len(result) != N:
                    result += arr[x-num][y]
                    num += 1
                pal = ''.join(result)
                if pal == pal[::-1]:
                    count += 1
    print("#{} {}".format(test_case, count))

