import sys
from collections import deque

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N, M = map(int, input().rstrip().split())

grid = [list(input()) for _ in range(N)]
root = [[(i, j) for j in range(M)] for i in range(N)]
visit = [[False for _ in range(M)] for _ in range(N)]
swan = []

def in_range(x, y):
    return (0 <= x < N and 0 <= y < M)

def find(x, y):
    if (x, y) == root[x][y]:
        return (x, y)
    root[x][y] = find(root[x][y][0], root[x][y][1])
    return root[x][y]

def union(x1, y1, x2, y2):
    x1, y1 = find(x1, y1)
    x2, y2 = find(x2, y2)
    root[x2][y2] = (x1, y1)

def bfs(melt):
    buf = deque()
    while melt:
        x, y = melt.popleft()
        grid[x][y] = "."
        union_list = []
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if in_range(nx, ny) and not visit[nx][ny] and grid[nx][ny] == "X":
                visit[nx][ny] = True
                buf.append((nx, ny))
            elif in_range(nx, ny) and grid[nx][ny] == ".":
                union_list.append((nx, ny))
        for a in union_list:
            bx, by = a[0], a[1]
            if find(bx, by) != find(x, y):
                union(bx, by, x, y)
    return buf


for i in range(N):
    for j in range(M):
        if grid[i][j] == "L":
            swan.append((i, j))
            grid[i][j] = "."
            if len(swan) == 2:
                break


melt = deque()
for i in range(N):
    for j in range(M):
        if not visit[i][j] and grid[i][j] == ".":
            q = deque()
            q.append((i, j))
            visit[i][j] = 1
            while q:
                x, y = q.popleft()
                root[x][y] = (i, j)
                for k in range(4):
                    ny, nx = y + dy[k], x + dx[k]
                    if in_range(nx, ny) and not visit[nx][ny] and grid[nx][ny] == ".":
                        visit[nx][ny] = True
                        q.append((nx, ny))
                    elif in_range(nx, ny) and not visit[nx][ny] and grid[nx][ny] == "X":
                        visit[nx][ny] = True
                        melt.append((nx, ny))


day = 0
while find(swan[0][0], swan[0][1]) != find(swan[1][0], swan[1][1]):
    melt = bfs(melt)
    day += 1

print(day)