import sys
sys.stdin = open("1284.txt")

for tc in range(1, int(input())+1):
    P, Q, R, S, W = list(map(int, input().split()))
    a = P * W
    if R < W:
        b = Q + (W - R) * S
    elif R > W:
        b = Q
    result = min(a, b)
    print('#{} {}'.format(tc, result))