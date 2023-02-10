from collections import deque
import os
import copy
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
grid = [list(map(int, input().rstrip().split())) for _ in range(N)]
virus = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ans = 0

for i in range(N):
    for j in range(M):
        if grid[i][j] == 2: virus.append((i, j))

def bfs(board):
    global ans
    cnt = 0
    q = deque([])
    for x in virus: q.append(x)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
                board[nx][ny] = 2
                q.append((nx, ny))
    for n in range(N):
        for m in range(M):
            if board[n][m] == 0: cnt += 1
    ans = max(ans, cnt)

def dfs(cnt):
    if cnt == 3:
        board_bfs = copy.deepcopy(grid)
        bfs(board_bfs)
        return
    else:
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 0:
                    grid[i][j] = 1
                    dfs(cnt + 1)
                    grid[i][j] = 0

dfs(0)
print(ans)