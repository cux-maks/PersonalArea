from collections import deque
import sys

input = sys.stdin.readline
N = int(input())

grid = [list(map(int, input().split())) for _ in range(N)]
d = [[-1 for _ in range(N)] for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

now_x, now_y = 0, 0
size, cnt = 2, 0
result = 0

for i in range(N):
    for j in range(N):
        if grid[i][j] == 9:
            now_x, now_y = i, j
            break

def bfs(a, b):
    global grid
    global size
    global d
    visited = [[False for _ in range(N)] for _ in range(N)]
    dist = []
    q = deque()
    q.append([a, b, 0])
    visited[a][b] = True
    d[a][b] = 0
    while q:
        x, y, distance = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if (not visited[nx][ny]) and grid[nx][ny] <= size:
                    visited[nx][ny] = True
                    q.append([nx, ny, distance + 1])
                    d[nx][ny] = distance + 1
                    if grid[nx][ny] < size and grid[nx][ny] != 0:
                        dist.append(distance + 1)
    dist.sort()
    return dist

while True:
    bfs_result = bfs(now_x, now_y)
    if len(bfs_result) == 0: break
    flag = 0
    for i in range(N):
        for j in range(N):
            if d[i][j] == bfs_result[0] and grid[i][j] < size and grid[i][j] != 0:
                result += d[i][j]
                grid[now_x][now_y] = 0
                now_x, now_y = i, j
                grid[now_x][now_y] = 9
                cnt += 1
                flag = 1
                if cnt == size:
                    size += 1
                    cnt = 0
                break
        if flag: break

print(result)