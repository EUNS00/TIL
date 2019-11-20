import queue
n, m, v = map(int, input().split()) #정점의 개수, 간선의 개수, 시작 번호

a = [list() for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    a[x].append(y)
    a[y].append(x)

for x in a:
    x.sort()

def bfs(start):
    q = queue.Queue()
    q.put(start)
    chk[start] = True

    while not q.empty():
        now = q.get()
        print(now, end=" ")
        for next in a[now]:
            if not chk[next]:
                chk[next] = True
                q.put(next)
    print()

def dfs(node):
    chk[node] = True
    print(node, end=" ")

    for next in a[node]:
        if not chk[next]:
            dfs(next)

chk = [False]*(n+1)
dfs(v)
print()
chk = [False]*(n+1)
bfs(v)