N = int(input())
if 0<=N<=10000:
    result = 0
    for i in range(N):
        N_0,N_1,N_2,N_3,N_4,N_5,N_6,N_7,N_8,N_9 = map(int,input().split())
        result = (N_0+N_1+N_2+N_3+N_4+N_5+N_6+N_7+N_8+N_9)/10
                
        print('#{} ' .format(N), end='')
        print('%.0f'%result)