from collections import deque
import sys
input = sys.stdin.readline

N = int(input().rstrip()) # 맵 크기 입력
grid = [list(map(int, input().rstrip().split())) for _ in range(N)] # 맵 입력
visit = [[False for _ in range(N)] for _ in range(N)] # 방문 리스트 생성
d = [(0, 1), (0, -1), (1, 0), (-1, 0)] # 상하좌우 변화
ans = sys.maxsize # 최대값

def grouping(start, grp): # 섬들을 그룹화 하는 함수

    q = deque([])
    q.append(start)
    visit[start[0]][start[1]] = True
    grid[start[0]][start[1]] = grp
    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not visit[nx][ny] and grid[nx][ny] == 1:
                grid[nx][ny] = grp
                visit[nx][ny] = True
                q.append((nx, ny))

def distance(start): # 그룹화한 섬들을 탐색을 통해 다른 섬까지의 거리를 계산하고, 최소값을 ans에 저장하는 함수
    global ans
    dist = [[-1 for _ in range(N)] for _ in range(N)]
    q = deque([])
    for i in range(N):
        for j in range(N):
            if grid[i][j] == start:
                q.append((i, j))
                dist[i][j] = 0
    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if grid[nx][ny] > 0 and grid[nx][ny] != start: # 다른 섬을 만난다면?
                    ans = min(ans, dist[x][y]) # 더 작은 값을 ans에 저장
                    return
                if grid[nx][ny] == 0 and dist[nx][ny] == -1: # 0(바다)를 만난다면? 
                    dist[nx][ny] = dist[x][y] + 1 # 이떄부터 거리를 1씩 증가하여 탐색
                    q.append((nx, ny))

g = 1
for i in range(N):
    for j in range(N):
        if grid[i][j] == 1 and not visit[i][j]:
            grouping((i, j), g)
            g += 1

for i in range(1, g + 1):
    distance(i)

print(ans)