import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().rstrip().split()) # N, M 입력
grid = [list(map(int, list(input().rstrip()))) for _ in range(N)] # grid 입력
visited = [[False for _ in range(M)] for _ in range(N)] # 방문 리스트 생성
zero = [[0 for _ in range(M)] for _ in range(N)] # 0의 개수 리스트 생성
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)] # x, y변화량 리스트 생성
group = 1 # 0 그룹 이름 생성
info = dict() # 0 그룹 저장할 딕셔너리 생성

def BFS(x, y): # 0 그룹: 0의 개수를 리턴하는 bfs함수 작성

    q = deque()
    q.append([x, y])
    visited[x][y] = True
    cnt = 1

    while q:
        x, y = q.pop()
        zero[x][y] = group 
        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= N or ny >= M: continue
            if visited[nx][ny]: continue
            if not grid[nx][ny]: 
                q.append([nx, ny])
                visited[nx][ny] = True
                cnt += 1
    return cnt

def check(x, y): # 갈 수 있는 방의 수를 리턴하는 함수 

    buf = set()
    for dx, dy in dir:
        nx, ny = x + dx, y + dy
        if nx < 0 or ny < 0 or nx >= N or ny >= M: continue
        if not zero[nx][ny]: continue
        buf.add(zero[nx][ny])
    cnt = 1
    for c in buf:
        cnt += info[c]
        cnt = cnt % 10
    return cnt

# 먼저 grid의 0들을 그룹으로 묶어서 딕셔너리에 그 그룹에 몇 개의 0이 들어있는지 저장한다.
for i in range(N):
    for j in range(M):
        if not grid[i][j] and not visited[i][j]: 
            cnt = BFS(i, j)
            info[group] = cnt
            group += 1

# grid의 상하좌우를 확인하며 0그룹이 있는지, 있다면 0이 몇 개 있는지를 더하여 ans에 저장한다.
ans = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if grid[i][j]:
            ans[i][j] = check(i, j)

# 결과값 출력
for i in range(N):
    print(''.join(map(str, ans[i])))