N = int(input())
if 1<=N<=1000:
    for num in range(1, N-1):
        if N%num==0:
            print(num, end=' ')
    print(N)