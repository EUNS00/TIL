# result = {}
# word = list(map(str, input().split()))
# word = ''.join(word)

# print(word)

# result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for r in result:
#     print(r, end=" ")

# word = list(map(str, input().split()))

# for num, w in enumerate(word):
#     if num==0 or num==3 or num==6:

#         print(w, end=" ")

# result = []
# num = list(map(int, input().split()))

# for n in num:
#     if n != 0:
#         result.append(n)
# result.reverse()
# for r in result:
#     print(r, end=" ")

# num = [85.6, 79.5, 83.1, 80.0, 78.2, 75.0]
# ban1, ban2 = list(map(int, input().split()))
# ban_sum = num[ban1-1] + num[ban2-1]
# print(round(ban_sum, 1))

# num = list(map(int, input().split()))
# num.sort()
# print(num[0])

# Min = 0
# Min_r = []
# Max = 0
# Max_r = []
# num = list(map(int, input().split()))
# for i in num:
#     if i>100:
#         Min_r.append(i)
#     elif i<100:
#         Max_r.append(i)
# Min_r.sort()
# Max_r.sort()
# if len(Min_r)==0:
#     print(Max_r[-1], 100)
# elif len(Max_r)==0:
#     print(100, Min_r[0])
# else:
#     print(Max_r[-1], Min_r[0])

# sum = 0
# avg = 0
# num = list(map(int, input().split()))
# for num, n in enumerate(num):
#     if num%2:
#         sum += n
#     else:
#         avg += n
# avg = round(avg/5, 1)
# print('sum : {}'.format(sum))
# print('avg : {}'.format(avg))

# num = list(map(int, input().split()))
# num.sort()
# num.reverse()
# for i in num:
#     print(i, end=" ")

result ={}
number = list(map(str, input().split()))
for n in number:
    if 65 <= ord(n) <= 90:
        if n not in result:
            result[n] = 1
        # else:
        #     result[num[1]] += 1

print(result)