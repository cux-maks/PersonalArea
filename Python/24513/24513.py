from collections import deque
import sys
input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().rstrip().split()) # 도시 크기 입력
grid = [] # 도시 입력 위한 리스트 생성
zombie_1 = None # 좀비1 시작 좌표
zombie_2 = None # 좀비2 시작 좌표
d = [(0, 1), (0, -1), (1, 0), (-1, 0)] # x, y 변화량

for i in range(N): # 도시 입력
    grid.append(list(map(int, input().rstrip().split())))
    for j in range(M):
        if grid[i][j] == 1: zombie_1 = (i, j) # 좀비1 시작 좌표 저장
        elif grid[i][j] == 2: zombie_2 = (i, j) # 좀비2 시작 좌표 저장


def bfs(): # BFS함수
    visit = [[0 for _ in range(M)] for _ in range(N)] # 거리 리스트 생성
    q = deque([])
    visit[zombie_1[0]][zombie_1[1]] = 1 # 좀비1은 양수
    visit[zombie_2[0]][zombie_2[1]] = -1 # 좀비2는 음수로 설정
    q.append((zombie_1[0], zombie_1[1], 1, 1)) # q에 x, y, 좀비종류, dist 추가
    q.append((zombie_2[0], zombie_2[1], 2, -1)) # q에 x, y, 좀비종류, dist 추가
    z1_cnt = 1 # 좀비1 카운트
    z2_cnt = 1 # 좀비2 카운트
    z3_cnt = 0 # 좀비3 카운트
    while q:
        x, y, z, dist = q.popleft() # x, y, 좀비종류, dist 뽑아오기
        if visit[x][y] == INF: continue # 거리가 INF면 그냥 continue
        for dx, dy in d: # 4방향 검사
            nx, ny = x + dx, y + dy
            if possible(nx, ny, visit): # 이동할 수 있는 곳이라면
                if visit[nx][ny] == 0: # 그리고 그곳이 방문한 적 없는 곳 이라면
                    if z == 1: # 방문한 적 없는 곳 이면서 좀비의 종류가 1이라면
                        visit[nx][ny] = dist + 1 # 해당 인덱스의 거리를 1 증가
                        z1_cnt += 1 # 좀비1 카운트 1 증가
                        q.append((nx, ny, 1, dist + 1)) # q에 추가
                    elif z == 2: # 좀비의 종류가 2라면
                        visit[nx][ny] = dist - 1 # 해당 인덱스의 거리를 -1 증가
                        z2_cnt += 1 # 좀비2 카운트 1증가
                        q.append((nx, ny, 2, dist - 1)) # q에 추가
                elif abs(visit[nx][ny]) == abs(dist) + 1 and ((visit[nx][ny] > 0 and z == 2) or (visit[nx][ny] < 0 and z == 1)): # 만약 동시에 도달했다면?
                    z3_cnt += 1 # 좀비3 카운트 1 증가
                    z1_cnt -= 1 # 좀비1 카운트 1 감소
                    # 여기에서 좀비1 카운트를 1 감소시킬 수 있는 이유?
                    # q에 좀비1을 먼저 원소로 대입했고, 이후에 좀비2를 대입했기 때문에
                    # q에서 뽑아오는 원소 순서상 좀비1이 움직인 이후에 좀비2가 움직인다.
                    # 따라서 좀비1 카운트를 감소시킬 수 있다.
                    visit[nx][ny] = INF # 해당 인덱스를 좀비3으로 표시하기 위해 INF로 교체
    return z1_cnt, z2_cnt, z3_cnt # 좀비 수 리턴

            
def possible(x, y, visit): # 방문 가능한지 판별하는 함수
    if x < 0 or y < 0 or x >= N or y >= M: return False # 도시 크기 범위를 벗어나면 False
    elif visit[x][y] == INF: return False # 좀비3 위치면 False
    elif grid[x][y] == -1: return False # 치료제 위치면 False
    return True # 아무것도 해당되지 않는다면 True

print(*bfs()) # 결과 출력