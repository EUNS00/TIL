import sys
sys.stdin = open("부분집합_input.txt")

TC  = int(input())
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
Len = len(num)

lst = []
for i in range(1 << Len):
    sub_lst = []
    for j in range(Len):
        if i & (1 << j):
            sub_lst.append(num[j])
    lst.append(sub_lst)


for tc in range(1, TC+1):
    N, K = map(int, input().split())

    len_lst = []
    for i in lst:
        if len(i) == N:
            len_lst.append(i)


    result = 0
    for i in len_lst:
        if sum(i) == K:
            result += 1

    print('#%s %d'%(tc, result))