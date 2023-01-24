import sys; INF = sys.maxsize

N = int(input())
M = int(input())

dist = [[INF for _ in range(N + 1)] for _ in range(N + 1)]

for _ in range(M):
    a, b, v = map(int, input().split())
    dist[a][b] = min(dist[a][b], v)

for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            if j != k:
                dist[j][k] = min(dist[j][k], dist[j][i] + dist[i][k])

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if dist[i][j] == INF: print(0, end = ' ')
        else: print(dist[i][j], end = ' ')
    print()