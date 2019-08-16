import sys
sys.stdin = open("0814_input.txt")

N = int(input())

for i in range(1, N+1):
    arr = [[i]*i for j in range(i)]
    # for j in range(1, i * i + 1):
    #     for x in range(len(arr)):
    #         for y in range(len(arr[x])):
    #             arr[x][y] = j
    #             continue

    print(arr)

