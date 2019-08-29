import sys
sys.stdin = open("금속막대_input.txt")

T = int(input())

for test_case in range(1, T+1):
    t = int(input())
    result = {}
    count = 0
    Fv = 0
    Screw = list(map(int, input().split()))