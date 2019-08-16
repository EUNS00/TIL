# a = 2
# b = 0
# for i in range(3):
#     b = 1
#     for i in range(5):
#         if a*b>9:
#             print(a, "*", b, "=", a * b, end="   ")
#         else:
#             print(a, "*", b, "= ", a * b, end="   ")
#         b += 1
#     print()
#     a+=1

# N = int(input())
# count = 0
# sum = 0
# for i in range(1, 10000):
#     if i%2:
#         count += 1
#         sum += i
#
#     if sum>=N:
#         print(count, sum)
#         break

# N = int(input())
# for i in range(1, N):
#     for i in range(i):
#         print('*',end="")
#     print()

N = int(input())
for i in range(N+1, 1):
    for i in range(i):
        print('*',end="")
    print()