import sys
sys.stdin = open("4828.txt")

for tc in range(1, int(input())+1):
    arr = []
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    result = arr[-1] - arr[0]
    print('#{} {}'.format(tc, result))