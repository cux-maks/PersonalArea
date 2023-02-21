import sys
input = sys.stdin.readline

R, C = map(int, input().rstrip().split())
grid = [list(input().rstrip()) for _ in range(R)]
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
visit = [False for _ in range(26)]
visit[ord(grid[0][0]) - 65] = True
ans = 0

def dfs(x, y, depth):
    
    global ans
    ans = max(ans, depth)

    for dx, dy in d:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < R and 0 <= ny < C and not visit[ord(grid[nx][ny]) - 65]:
            visit[ord(grid[nx][ny]) - 65] = True
            dfs(nx, ny, depth + 1)
            visit[ord(grid[nx][ny]) - 65] = False

dfs(0, 0, 1)
print(ans)