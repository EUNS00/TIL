def f(k):
    if k <=1 :
        return 1
    else:
        return f(k-1) + 2*f(k-2)

import sys
sys.stdin = open("종이.txt")
T = int(input())

for t in range(1, T+1):
    N = int(input())

    print("#{} {}".format(t, f(N//10)))