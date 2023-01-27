from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
grid = [list(map(int, input().rstrip().split())) for _ in range(N)]
distance = [[-1 for _ in range(M)] for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

q = deque([])

def possible(a, b):
    return 0 <= a < N and 0 <= b < M

for i in range(N):
    for j in range(M):
        if grid[i][j] == 2:
            q.append((i, j))
            visited[i][j] = True
            distance[i][j] = 0
        elif not grid[i][j]:
            distance[i][j] = 0

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if possible(nx, ny) and not visited[nx][ny] and grid[nx][ny] == 1:
            q.append((nx, ny))
            visited[nx][ny] = True
            distance[nx][ny] = distance[x][y] + 1

for x in distance:
    print(*x)