import sys
input = sys.stdin.readline

N = int(input())
grid = [list(map(int, input().rstrip().split())) for _ in range(N)]
ans = 0

def dfs(x, y, way):
    global ans
    if x == N - 1 and y == N - 1:
        ans += 1
        return
    nx, ny = x + 1, y + 1
    if nx < N and ny < N:
        if not grid[nx][ny] and not grid[nx - 1][ny] and not grid[nx][ny - 1]:
            dfs(nx, ny, 2)
    if way == 1 or way == 2:
        nx, ny = x, y + 1
        if ny < N:
            if not grid[nx][ny]:
                dfs(nx, ny, 1)
    if way == 2 or way == 3:
        nx, ny = x + 1, y
        if nx < N:
            if not grid[nx][ny]:
                dfs(nx, ny, 3)

dfs(0, 1, 1)
print(ans)