import sys
input = sys.stdin.readline

N, M, R = map(int, input().rstrip().split())
item = list(map(int, input().rstrip().split()))
graph = [[sys.maxsize for _ in range(N)] for _ in range(N)]

for _ in range(R):
    a, b, l = map(int, input().rstrip().split())
    graph[a - 1][b - 1] = min(graph[a - 1][b - 1], l)
    graph[b - 1][a - 1] = min(graph[b - 1][a - 1], l)

for k in range(N):
    for a in range(N):
        for b in range(N):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
            if a == b: graph[a][b] = 0

result = 0

for i in range(N):
    buf = 0
    for j in range(N):
        if graph[i][j] <= M: buf += item[j]
    result = max(result, buf)

print(result)