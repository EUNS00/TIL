import sys
sys.stdin = open("특이한자석.txt")

for tc in range(1, int(input())+1):
    K = int(input())

    Mag = [0]
    for _ in range(4):
        arr = list(map(int, input().split()))
        Mag.append(arr)
    # print(Mag)

    for _ in range(K):
        test = list(map(int, input().split()))
        # print(test)
        # print(Mag[1][2], Mag[2][6], Mag[2][2], Mag[3][6], Mag[3][2], Mag[4][6])
        if Mag[1][2] == Mag[2][6] and Mag[2][2] == Mag[3][6] and Mag[3][2] == Mag[4][6]:
            if test[1] == 1:
                Mag[test[0]].insert(Mag[test[0]][0], Mag[test[0]].pop(-1))
            elif test[1] == -1:
                Mag[test[0]].append(Mag[test[0]].pop(0))
        elif Mag[1][2] != Mag[2][6] and Mag[2][2] == Mag[3][6] and Mag[3][2] == Mag[4][6]:
            if test[0] == 3 or test[0] == 4:
                if test[1] == 1:
                    Mag[test[0]].insert(Mag[test[0]][0], Mag[test[0]].pop(-1))
                elif test[1] == -1:
                    Mag[test[0]].append(Mag[test[0]].pop(0))
            else:
                if test[1] == 1:
                    if test[0] == 1:
                        Mag[1].insert(Mag[1][0], Mag[1].pop(-1))
                        Mag[2].append(Mag[2].pop(0))
                    elif test[0] == 2:
                        Mag[2].insert(Mag[2][0], Mag[2].pop(-1))
                        Mag[1].append(Mag[1].pop(0))
                elif test[1] == -1:
                    if test[0] == 1:
                        Mag[1].append(Mag[1].pop(0))
                        Mag[2].insert(Mag[2][0], Mag[2].pop(-1))
                    elif test[0] == 2:
                        Mag[2].append(Mag[2].pop(0))
                        Mag[1].insert(Mag[1][0], Mag[1].pop(-1))
        elif Mag[1][2] == Mag[2][6] and Mag[2][2] != Mag[3][6] and Mag[3][2] == Mag[4][6]:
            if test[0] == 1 or test[0] == 4:
                if test[1] == 1:
                    Mag[test[0]].insert(Mag[test[0]][0], Mag[test[0]].pop(-1))
                elif test[1] == -1:
                    Mag[test[0]].append(Mag[test[0]].pop(0))
            elif test[1] == 1:
                if test[0] == 2:
                    Mag[2].insert(Mag[2][0], Mag[2].pop(-1))
                    Mag[3].append(Mag[3].pop(0))
                elif test[0] == 3:
                    Mag[3].insert(Mag[3][0], Mag[3].pop(-1))
                    Mag[2].append(Mag[2].pop(0))
            elif test[1] == -1:
                if test[0] == 2:
                    Mag[2].append(Mag[2].pop(0))
                    Mag[3].insert(Mag[3][0], Mag[3].pop(-1))
                elif test[0] == 3:
                    Mag[3].append(Mag[3].pop(0))
                    Mag[2].insert(Mag[2][0], Mag[2].pop(-1))
        elif Mag[1][2] == Mag[2][6] and Mag[2][2] == Mag[3][6] and Mag[3][2] != Mag[4][6]:
            if test[0] == 1 or test[0] == 2:
                if test[1] == 1:
                    Mag[test[0]].insert(Mag[test[0]][0], Mag[test[0]].pop(-1))
                elif test[1] == -1:
                    Mag[test[0]].append(Mag[test[0]].pop(0))
            elif test[1] == 1:
                if test[0] == 3:
                    Mag[3].insert(Mag[3][0], Mag[3].pop(-1))
                    Mag[4].append(Mag[4].pop(0))
                elif test[0] == 4:
                    Mag[4].insert(Mag[4][0], Mag[4].pop(-1))
                    Mag[3].append(Mag[3].pop(0))
            elif test[1] == -1:
                if test[0] == 3:
                    Mag[3].append(Mag[3].pop(0))
                    Mag[4].insert(Mag[4][0], Mag[4].pop(-1))
                elif test[0] == 4:
                    Mag[4].append(Mag[4].pop(0))
                    Mag[3].insert(Mag[3][0], Mag[3].pop(-1))
        elif Mag[1][2] != Mag[2][6] and Mag[2][2] != Mag[3][6] and Mag[3][2] == Mag[4][6]:
            if test[0] == 4:
                if test[1] == 1:
                    Mag[test[0]].insert(Mag[test[0]][0], Mag[test[0]].pop(-1))
                elif test[1] == -1:
                    Mag[test[0]].append(Mag[test[0]].pop(0))
            elif test[1] == 1:
                if test[0] == 1 or test[0] == 3:
                    Mag[1].insert(Mag[1][0], Mag[1].pop(-1))
                    Mag[2].append(Mag[2].pop(0))
                    Mag[3].insert(Mag[3][0], Mag[3].pop(-1))
                elif test[0] == 2:
                    Mag[1].append(Mag[1].pop(0))
                    Mag[2].insert(Mag[2][0], Mag[2].pop(-1))
                    Mag[3].append(Mag[3].pop(0))
            elif test[1] == -1:
                if test[0] == 1 or test[0] == 3:
                    Mag[1].append(Mag[1].pop(0))
                    Mag[2].insert(Mag[2][0], Mag[2].pop(-1))
                    Mag[3].append(Mag[3].pop(0))
                elif test[0] == 2:
                    Mag[1].insert(Mag[1][0], Mag[1].pop(-1))
                    Mag[2].append(Mag[2].pop(0))
                    Mag[3].insert(Mag[3][0], Mag[3].pop(-1))
        elif Mag[1][2] != Mag[2][6] and Mag[2][2] == Mag[3][6] and Mag[3][2] != Mag[4][6]:
            if test[1] == 1:
                if test[0] == 1:
                    Mag[1].insert(Mag[1][0], Mag[1].pop(-1))
                    Mag[2].append(Mag[2].pop(0))
                elif test[0] == 2:
                    Mag[2].insert(Mag[2][0], Mag[2].pop(-1))
                    Mag[1].append(Mag[1].pop(0))
                elif test[0] == 3:
                    Mag[3].insert(Mag[3][0], Mag[3].pop(-1))
                    Mag[4].append(Mag[4].pop(0))
                elif test[0] == 4:
                    Mag[4].insert(Mag[4][0], Mag[4].pop(-1))
                    Mag[3].append(Mag[3].pop(0))
            elif test[1] == -1:
                if test[0] == 1:
                    Mag[1].append(Mag[1].pop(0))
                    Mag[2].insert(Mag[2][0], Mag[2].pop(-1))
                elif test[0] == 2:
                    Mag[2].append(Mag[2].pop(0))
                    Mag[1].insert(Mag[1][0], Mag[1].pop(-1))
                elif test[0] == 3:
                    Mag[3].append(Mag[3].pop(0))
                    Mag[4].insert(Mag[4][0], Mag[4].pop(-1))
                elif test[0] == 4:
                    Mag[4].append(Mag[4].pop(0))
                    Mag[3].insert(Mag[3][0], Mag[3].pop(-1))
        elif Mag[1][2] == Mag[2][6] and Mag[2][2] != Mag[3][6] and Mag[3][2] != Mag[4][6]:
            if test[0] == 1:
                if test[1] == 1:
                    Mag[test[0]].insert(Mag[test[0]][0], Mag[test[0]].pop(-1))
                elif test[1] == -1:
                    Mag[test[0]].append(Mag[test[0]].pop(0))
            elif test[1] == 1:
                if test[0] == 2 or test[0] == 4:
                    Mag[2].insert(Mag[2][0], Mag[2].pop(-1))
                    Mag[3].append(Mag[3].pop(0))
                    Mag[4].insert(Mag[4][0], Mag[4].pop(-1))
                elif test[0] == 3:
                    Mag[2].append(Mag[2].pop(0))
                    Mag[3].insert(Mag[3][0], Mag[3].pop(-1))
                    Mag[4].append(Mag[4].pop(0))
            elif test[1] == -1:
                if test[0] == 2 or test[0] == 4:
                    Mag[2].append(Mag[2].pop(0))
                    Mag[3].insert(Mag[3][0], Mag[3].pop(-1))
                    Mag[4].append(Mag[4].pop(0))
                elif test[0] == 3:
                    Mag[2].insert(Mag[2][0], Mag[2].pop(-1))
                    Mag[3].append(Mag[3].pop(0))
                    Mag[4].insert(Mag[4][0], Mag[4].pop(-1))
        elif Mag[1][2] != Mag[2][6] and Mag[2][2] != Mag[3][6] and Mag[3][2] != Mag[4][6]:
            if test[1] == 1:
                if test[0] == 2 or test[0] == 4:
                    Mag[1].append(Mag[1].pop(0))
                    Mag[2].insert(Mag[2][0], Mag[2].pop(-1))
                    Mag[3].append(Mag[3].pop(0))
                    Mag[4].insert(Mag[4][0], Mag[4].pop(-1))
                elif test[0] == 1 or test[0] == 3:
                    # Mag[1].insert(Mag[1][0], Mag[1].pop(-1))
                    Mag[1].insert(Mag[1][1], Mag[1].pop(-1))
                    Mag[2].append(Mag[2].pop(0))
                    Mag[3].insert(Mag[3][0], Mag[3].pop(-1))
                    Mag[4].append(Mag[4].pop(0))
            elif test[1] == -1:
                if test[0] == 2 or test[0] == 4:
                    Mag[1].insert(Mag[1][0], Mag[1].pop(-1))
                    Mag[2].append(Mag[2].pop(0))
                    Mag[3].insert(Mag[3][0], Mag[3].pop(-1))
                    Mag[4].append(Mag[4].pop(0))
                elif test[0] == 1 or test[0] == 3:
                    Mag[1].append(Mag[1].pop(0))
                    Mag[2].insert(Mag[2][0], Mag[2].pop(-1))
                    Mag[3].append(Mag[3].pop(0))
                    Mag[4].insert(Mag[4][1], Mag[4].pop(-1))
        # print(Mag)

    sum = 0
    if Mag[1][0] == 1:
        sum += 1
    if Mag[2][0] == 1:
        sum += 2
    if Mag[3][0] == 1:
        sum += 4
    if Mag[4][0] == 1:
        sum += 8
    print('#{} {}'.format(tc, sum))
    # print()