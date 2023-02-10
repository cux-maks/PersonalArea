from collections import deque
import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]

while True:

    w, h = map(int, input().rstrip().split())
    if not w and not h: break
    grid = [list(map(int, input().rstrip().split())) for _ in range(h)]
    visit = [[False for _ in range(w)] for _ in range(h)]
    ans = 0
    q = deque([])

    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1 and not visit[i][j]:
                q.append((i, j))
                visit[i][j] = True
                while q:
                    x, y = q.popleft()
                    for d in range(8):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0 <= nx < h and 0 <= ny < w and not visit[nx][ny] and grid[nx][ny]:
                            visit[nx][ny] = True
                            q.append((nx, ny))
                ans += 1

    print(ans)