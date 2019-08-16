# count = 0
# while count<10:
#     N = int(input('number? '))
#     if N>0:
#         print('positive integer')
#     elif N<0:
#         print('negative number')
#     else:
#         break

# result = 0
# count = 0
# num = list(map(int, input().split()))
# for i in num:
#     result+=i
#     count+=1
# print(result)
# print(round(result/count, 1))

# count = 0

# while count<10000:
#     N = int(input())
#     if N%3==0:
#         print(N//3)
#     if N==-1:
#         break
#     count +=1

# count = 0

# while count<20:
#     print('1. Korea\n2.USA\n3.Japan\n4.China')
#     N = int(input('number? '))
#     if N==1:
#         print('Seoul')
#     elif N==2:
#         print('Washington')
#     elif N==3:
#         print('Tokyo')
#     elif N==4:
#         print('Beijing')
#     else:
#         print('none')
#         break


# count = 0
# N = input()
# while count<20:
#     print(N,end='')
#     count+=1

# for i in range(10, 21):
#     print(i,end=' ')
# N = int(input())

# for i in range(1, N+1):
#     if i%2==0:
#         print(i,end=' ')

# N = int(input())
# if N<=100:
#     sum = 0
#     for i in range(N, 100+1):
#         sum += i
#     print(sum)

# num = list(map(int, input().split()))
# mul_3=0
# mul_5=0
# for i in num:
#     if i%3==0:
#         mul_3+=1
#     if i%5==0:
#         mul_5+=1
# print('Multiples of 3 : {}'.format(mul_3))
# print('Multiples of 5 : {}'.format(mul_5))
# Sum = 0
# N = int(input())
# num = list(map(int, input().split()))
# if len(num)==N:
#     for i in num:
#         Sum+=i
# A = round(Sum/N,1)
# print('avg : {}'.format(A))
# if A > 80:
#     print('pass')
# else:
#     print('fail')

# N = int(input())
# for i in range(1, N+1):
#     for i in range(i):
#         print('*',end="")
#     print()

# N = int(input())
# for i in range(N, 0, -1):
#     for i in range(i):
#         print('*',end="")
#     print()
# for i in range(1, N+1):
#     for i in range(i):
#         print('*',end="")
#     print()

# count = 0 
# N = int(input())
# for i in range(N, 0, -1):
#     num=0
#     for i in range(i):
#         if num==0:
#             print(' '*count,end="")
#             num+=1
#         print('*',end="")
#     count+=1    
#     print()


# count = 0 
# N = int(input())
# for i in range(N+(N-1), 0, -2):
#     num=0
#     for i in range(i):
#         if num==0:
#             print(' '*count,end="")
#             num+=1
#         print('*',end="")
#     count+=1    
#     print()
# word=65
# N = int(input())
# for i in range(N, 0, -1):
#     for i in range(i):
#         print(ord(word),end="")
#         word+=1
#     print()

# word=65
# num = 1
# N = int(input())
# for i in range(N, 0, -1):
#     for i in range(i):
#         print(num ,end=" ")
#         num += 1
#     for i in range(N-i):
#         print(chr(word) ,end=" ")
#         word += 1
#     print()
 
def printArray(ary):
    for i in ary:
        for j in i:
            print('%3d' % j, end=' ')
        print()
 
def snailArray(ary):
 
    offset=0
    num=1
    nrows=5
    ncols=5
 
    while nrows>0 and ncols>0:
 
        for i in range(offset,offset+ncols):
            ary[offset][i]=num
            num+=1
 
        for i in range(offset+1,offset+nrows):
            ary[i][offset+ncols-1]=num
            num+=1
 
        for i in range(offset+ncols-2,offset-1,-1):
            ary[offset+nrows-1][i]=num
            num+=1
 
        for i in range(offset+nrows-2, offset, -1):
            ary[i][offset]=num
            num+=1
 
        offset+=1
        nrows-=2
        ncols-=2
 
 
ary = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
 
snailArray(ary)
printArray(ary)

