import sys
sys.stdin = open("숫자만들기.txt")

for tc in range(1, int(input())+1):
    N = int(input())
    a = list(map(int, input().split()))
    num = list(map(int, input().split()))
