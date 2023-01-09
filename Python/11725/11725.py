import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input())

tree = [[] for _ in range(N + 1)]
parents = [0 for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def DFS(start):
    global tree, parents
    for i in tree[start]:
        if parents[i] == 0:
            parents[i] = start
            DFS(i)

DFS(1)

for i in range(2, N + 1): print(parents[i])