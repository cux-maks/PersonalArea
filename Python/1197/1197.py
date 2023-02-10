import sys
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b: parent[b] = a
    else: parent[a] = b

V, E = map(int, input().rstrip().split())
parent = [i for i in range(V + 1)]
graph = []
result = 0

for _ in range(E):
    a, b, c = map(int, input().split())
    graph.append((c, a, b))

graph.sort()

for i in range(E):
    c, a, b = graph[i]
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += c

print(result)