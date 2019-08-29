import sys
sys.stdin = open("금속막대_input.txt")

T = int(input())

for test_case in range(1, T+1):
    t = int(input())
    result = {}
    count = 0
    Fv = 0
    Screw = list(map(int, input().split()))
    print('#{}'.format(test_case), end=" ")
    for num, s in enumerate(Screw):
        if num%2==0:
            result[s] = Screw[num+1]
    for key, value in result.items():
        if key not in result.values():
            print(key, value, end=" ")
            Fv = value
    while count != int(len(Screw)/2-1):
        count += 1
        print(Fv, result.get(Fv), end=" ")
        Fv = result.get(Fv)
    print()
