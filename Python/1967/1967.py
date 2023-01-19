import sys; input = sys.stdin.readline; sys.setrecursionlimit(10 ** 9)

N = int(input())
tree = [[] for _ in range(N + 1)]

def dfs(x, v):
    for i in tree[x]:
        a, b = i
        if dist[a] == -1:
            dist[a] = v + b
            dfs(a, v + b)

for _ in range(N - 1):
    p, c, v = map(int, input().split())
    tree[p].append([c, v])
    tree[c].append([p, v])

dist = [-1 for _ in range(N + 1)]
dist[1] = 0
dfs(1, 0)

start = dist.index(max(dist))
dist = [-1 for _ in range(N + 1)]
dist[start] = 0
dfs(start, 0)

print(max(dist))