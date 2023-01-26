T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    grid = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
    for i in range(1, M - N + 2): grid[1][i] = i
    for i in range(1, N + 1): grid[i][i] = 1
    for i in range(2, N + 1):
        for j in range(i + 1, i + (M - N) + 1):
            grid[i][j] = grid[i][j - 1] + grid[i - 1][j - 1]
    print(grid[N][M])