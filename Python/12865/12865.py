import sys; input = sys.stdin.readline

N, K = map(int, input().split())
things = [[0, 0]]
result = [[0 for _ in range(K + 1)] for _ in range(N + 1)]


for _ in range(N):
    things.append(list(map(int, input().split())))

for i in range(1, N + 1):
    weight = things[i][0]
    value = things[i][1]
    for j in range(1, K + 1):
        if j < weight:
            result[i][j] = result[i - 1][j]
        else:
            result[i][j] = max(value + result[i - 1][j - weight], result[i - 1][j])

print(result[N][K])