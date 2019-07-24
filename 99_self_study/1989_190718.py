N = int(input())
for number in range(N):
    print(f'#{number+1}', end=' ')
    word = input()
    if word == word[::-1]:
        TF = 1
    else:
        TF = 0
    print(TF)