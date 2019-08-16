import sys
sys.stdin = open("2차_배열.txt")

def isWall(x, y):
    if x < 0 or x >= 5 : return True
    if y < 0 or y >= 5 : return True
    return False

def calabs(y, x):
    if y - x > 0: return y - x
    else: return x - y

arr = [[0 for _ in range(5)] for _ in range(5)]
for i in range(5):
    arr[i] = list(map(int, input().split()))

print(arr)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

sum = 0
for x in range(len(arr)):
    for y in range(len(arr[x])):
        for i in range(4):
            arr[x][y] = 5
            testX = x + dx[i]
            testY = y + dy[i]
            if isWall(testX, testY) == False:
                sum += calabs(arr[y][x], arr[testY][testX])
print(arr)