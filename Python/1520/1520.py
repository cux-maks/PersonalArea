import sys; input = sys.stdin.readline; sys.setrecursionlimit(10 ** 8)

N, M = map(int, input().rstrip().split())
grid = [list(map(int, input().rstrip().split())) for _ in range(N)]
dp = [[-1 for _ in range(M)] for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    if x == N - 1 and y == M - 1: return 1
    if dp[x][y] != -1: return dp[x][y]
    dp[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if grid[nx][ny] < grid[x][y]:
                dp[x][y] += dfs(nx, ny)
    return dp[x][y]

print(dfs(0, 0))