N = int(input())
count = 1

for i in range(2, N+1):
    if N%i == 0 and i<N:
        count += 1
        print(i)
        continue
    elif N%i == 0 and count ==1:
        print('소수입니다.')