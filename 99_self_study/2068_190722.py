N = int(input())
if 0<=N<=10000:
    maxy = 0
    for i in range(N):
        N_0,N_1,N_2,N_3,N_4,N_5,N_6,N_7,N_8,N_9 = map(int,input().split())
        maxy = N_1
        if maxy < N_1:
            maxy = N_1    
        if maxy < N_2:
            maxy = N_2
        if maxy < N_3:
            maxy = N_3
        if maxy < N_4:
            maxy = N_4
        if maxy < N_5:
            maxy = N_5
        if maxy < N_6:
            maxy = N_6
        if maxy < N_7:
            maxy = N_7
        if maxy < N_8:
            maxy = N_8
        if maxy < N_9:
            maxy = N_9
            
        print(f'#{i+1} {maxy}')