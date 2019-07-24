N = int(input())
pra = []
for number in range(N):
    print(f'#{number+1}')
    num_z = 1
    num = int(input())
    for num_one in range(num):
        num_tre = 0
        pra.append(f'{num_z}')
        if num_one > 1:
            for num_two in pra:
                print(int(num_two) + int(num_tre), end=' ')
                num_tre = num_two
        else:
            for num_two in pra:
                print(int(num_two), end=' ')
        print(num_one)