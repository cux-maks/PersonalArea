from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
grid = [list(map(int, input().rstrip().split())) for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
T = 0

def possible(x, y):
    return 0 <= x < N and 0 <= y < M

while True:
    q = deque([])
    cheeze = [[0 for _ in range(M)] for _ in range(N)]
    cheeze[0][0] = 1
    q.append((0, 0))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if possible(nx, ny) and not cheeze[nx][ny]:
                if grid[nx][ny]:
                    grid[nx][ny] += 1
                else:
                    cheeze[nx][ny] = 1
                    q.append((nx, ny))

    flag = True
    for i in range(N):
        for j in range(M):
            if grid[i][j] >= 3:
                grid[i][j] = 0
            elif 0 < grid[i][j]:
                flag = False
                grid[i][j] = 1
    
    T += 1
    if flag:
        print(T)
        break