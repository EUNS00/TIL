# N = int(input())
# number = []
# for i in range(N+1):
#     number+=str(i)

# rev = number[::-1]
# for i in rev:
#     if i == 0:
#         print(i, end='')
#     else:
#         print(i, end=' ')

num=int(input())
 
for i in range(num, -1, -1):
    print(i, end=' ')