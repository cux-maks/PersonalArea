N, M = map(int, input().split())
b = [0 for _ in range(N)]
for _ in range(M):
    i, j, k = map(int, input().split())
    for x in range(i - 1, j):
        b[x] = k
print(*b)