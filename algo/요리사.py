import sys
sys.stdin = open("요리사.txt")

import itertools

def cal(lines, a, b):
    return lines[int(a)][int(b)]

def bruteforce(lines, n):
    count = n // 2
    incredients = range(n)
    combis = itertools.combinations(incredients, count)
    incredients = set(incredients)
    min_result = 9999

    for combi in combis:
        afood = set(list(combi))
        bfood = list(incredients - afood)
        afood_total = 0
        bfood_total = 0

        if combi[0] != 0:
            break

        afood = list(afood)
        afood_combi = itertools.combinations(afood, 2)
        for coma in afood_combi:
            afood_total += cal(lines, coma[0], coma[1])

        bfood_combi = itertools.combinations(bfood, 2)
        for comb in bfood_combi:
            bfood_total += cal(lines, comb[0], comb[1])

        if abs(afood_total - bfood_total) < min_result:
            min_result = abs(afood_total - bfood_total)

    return min_result



for tc in range(1, int(input())+1):
    n = int(input().strip())
    lines = []
    for i in range(n):
        arr = list(map(int, input().strip().split()))
        lines.append(arr)

    for i in range(n):
        for j in range(n):
            if j > i:
                lines[i][j] = lines[i][j] + lines[j][i]
                lines[j][i] = 0
    print('#{0} {1}'.format(tc, bruteforce(lines,n)))