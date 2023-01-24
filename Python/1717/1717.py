import sys;
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

N, M = map(int, input().split())
parent = [i for i in range(N + 1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b: parent[b] = a
    else: parent[a] = b

for _ in range(M):
    f, a, b = map(int, input().rstrip().split())
    if f == 0:
        union(a, b)
    elif f == 1:
        af = find(a)
        bf = find(b)
        if af != bf: print("NO")
        else: print("YES")