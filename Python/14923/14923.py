from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
Hx, Hy = map(int, input().rstrip().split())
Ex, Ey = map(int, input().rstrip().split())
grid = [list(map(int, input().rstrip().split())) for _ in range(N)]
visit = [[[0 for _ in range(2)] for _ in range(M)] for _ in range(N)]
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

q = deque([])
q.append((Hx - 1, Hy - 1, 1))

while q:
    x, y, z = q.popleft()
    if x == Ex - 1 and y == Ey - 1:
        print(visit[x][y][z])
        exit(0)
    for dx, dy in d:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < N and 0 <= ny < M:
            if grid[nx][ny] == 0 and visit[nx][ny][z] == 0:
                visit[nx][ny][z] = visit[x][y][z] + 1
                q.append((nx, ny, z))
            if grid[nx][ny] == 1 and z == 1:
                visit[nx][ny][z - 1] = visit[x][y][z] + 1
                q.append((nx, ny, z - 1))

print(-1)