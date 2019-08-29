import sys
sys.stdin = open("2001_input.txt")

def g(grid, i, j, M) :                     # (i,j)를 (0,0)으로 하는 M by M 부분행렬의 합 구하기
    Sum = 0
    for k in range(M) :
        Sum += sum(grid[i+k][j:j+M])
    return Sum

def f(grid, N, M) :                       # N by N 행렬 내 M by M 부분 행렬들의 합을 list로 반환
    Sums = []
    for i in range(N-M+1) :
        for j in range(N-M+1) :
            Sums . append( g(grid, i, j, M) )
    return Sums

for T in range(int(input())) :
    NM = input().split(sep=' ')
    N=int(NM[0]) ; M=int(NM[1])
    grid=[]
    for n in range(N) :
        grid.append(list(map(int,input().split(sep=' '))))
    print( '#{} {}'.format (T+1, max(f(grid, N, M)) ))