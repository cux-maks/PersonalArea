from collections import deque
import sys; input = sys.stdin.readline

N, M, K = map(int, input().split())
grid = [list(input().strip()) for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

check = False

def bfs():

    visited = [[[0 for _ in range(K + 1)] for _ in range(M)] for _ in range(N)]
    q = deque()
    q.append([0, 0, K])
    visited[0][0][K] = 1

    while q:
        x, y, z = q.popleft()
        if x == N - 1 and y == M - 1: return visited[x][y][z]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if grid[nx][ny] == '0' and visited[nx][ny][z] == 0:
                    q.append([nx, ny, z])
                    visited[nx][ny][z] = visited[x][y][z] + 1
                if grid[nx][ny] == '1' and z > 0 and visited[nx][ny][z - 1] == 0:
                    q.append([nx, ny, z - 1])
                    visited[nx][ny][z - 1] = visited[x][y][z] + 1
    
    return -1

print(bfs())