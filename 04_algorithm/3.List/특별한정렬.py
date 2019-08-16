import sys
sys.stdin = open("특별한정렬_input.txt")

T = int(input())
if 1<=T<=50:
    for test_case in range(1, T+1):
        N = int(input())
        B = list(map(int, input().split()))
        if len(B)==N:
            print('#', end="")
            print(test_case, end=" ")
            for num, S in enumerate(B*1):
                if len(B)%2==0:
                    B.sort()
                    if B != []:
                        A = B.pop()
                elif len(B)%2==1:
                    B.reverse()
                    A = B.pop()
                if num<10:
                    print(A, end=" ")
            print()