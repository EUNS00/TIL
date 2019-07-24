N = int(input())
if 10<=N<=1000:
    for num in range(1, N+1):
        if (num//10==3 or num//10==6 or num//10==9) or  (num%10==3 or num%10==6 or num%10==9):
            if (num//10==3 or num//10==6 or num//10==9) and  (num%10==3 or num%10==6 or num%10==9):
                print('--', end = ' ')
            else:
                print('-', end = ' ')
        else:
            print(num, end = ' ')