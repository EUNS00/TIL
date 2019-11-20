import sys
sys.stdin = open("4837.txt")

for tc in range(1, int(input())+1):
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    N, K = list(map(int, input().split()))
    num2 = len(num)

    for i in range(1 << num2):
        print(i)