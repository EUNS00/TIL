import sys
sys.stdin = open("4831.txt")

for tc in range(1, int(input())+1):
    K, N, M = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    bus = 0
    bus_stop = []
    while bus <= N:
        bus += K
        if bus >= N:
            break
        count = 0
        for _ in range(K):
            if bus in arr:
                bus_stop.append(bus)
                break
            else:
                bus -= 1
                count += 1
        if count == K:
            bus_stop.append(0)
            break

    if 0 in bus_stop:
        print('#{} 0'.format(tc))
    else:
        print('#{} {}'.format(tc, len(bus_stop)))