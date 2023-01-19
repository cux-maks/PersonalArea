import sys; sys.setrecursionlimit(10 ** 9)

N = int(input())
tree = [[] for _ in range(N + 1)]

def dfs(x, v):
    for i in tree[x]:
        a, b = i
        if dist[a] == -1:
            dist[a] = v + b
            dfs(a, v + b)

for _ in range(N):
    x = list(map(int, input().split()))
    idx = 1
    while True:
        if x[idx] == -1: break
        tree[x[0]].append((x[idx], x[idx + 1]))
        tree[x[idx]].append((x[0], x[idx + 1]))
        idx += 2

dist = [-1 for _ in range(N + 1)]
dist[1] = 0
dfs(1, 0)

start = dist.index(max(dist))
dist = [-1 for _ in range(N + 1)]
dist[start] = 0
dfs(start, 0)

print(max(dist))