T = int(input())
if 0<=T<=10000:
    for i in range(1):
        result = 0
        num = list(map(int, input().split()))
        num2 = sorted(num)
        result = num2[T//2]

        print(f'{result}')
