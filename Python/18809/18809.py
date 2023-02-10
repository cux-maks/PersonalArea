from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline

N, M, G, R = map(int, input().rstrip().split()) # N, M, G, R 입력
garden = []
broth = []
d = [(0, 1), (0, -1), (1, 0), (-1, 0)] # x, y 변화량
INF = sys.maxsize
ans = 0

for i in range(N): # 정원 입력
    garden.append(list(map(int, input().rstrip().split())))
    for j in range(M):
        if garden[i][j] == 2: # 배양액을 뿌릴 수 있는 땅이면 ?
            broth.append((i, j)) # 배양액 리스트에 추가

def select(sel, now, pos, g_cnt, r_cnt): # 선택된 조합에서 초록색과 빨간색 배양액의 수에 맞게 선택하는 DFS알고리즘

    global ans

    if now == G + R:
        ans = max(ans, bfs(pos, sel)) # bfs탐색 결과와 ans중 최대값을 저장
        return

    if g_cnt > 0:
        g_cnt -= 1
        sel[now] = 1
        select(sel, now + 1, pos, g_cnt, r_cnt)
        g_cnt += 1
    
    if r_cnt > 0:
        r_cnt -= 1
        sel[now] = -1
        select(sel, now + 1, pos, g_cnt, r_cnt)
        r_cnt += 1

def bfs(pos, color): # 전달된 배양액의 위치에 따른 꽃 생성 개수를 bfs탐색을 통해 도출하는 함수

    visit = [[0 for _ in range(M)] for _ in range(N)]
    q = deque([])

    for i in range(G + R):
        x, y = pos[i]
        visit[x][y] = color[i]
        q.append((x, y, color[i]))

    flower = 0

    while q:
        x, y, c = q.popleft()
        if visit[x][y] == INF: continue
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if possible(nx, ny, visit):
                if visit[nx][ny] == 0:
                    if c < 0:
                        visit[nx][ny] = c - 1
                        q.append((nx, ny, c - 1))
                    else:
                        visit[nx][ny] = c + 1
                        q.append((nx, ny, c + 1))
                elif abs(visit[nx][ny]) == abs(c) + 1 and ((visit[nx][ny] < 0 and c > 0) or (visit[nx][ny] > 0 and c < 0)): # 두 배양액이 동시에 도달한 칸이면
                    flower += 1 # 꽃의 수 추가
                    visit[nx][ny] = INF
    
    return flower

def possible(x, y, visit): # 해당 정원 위치에 갈 수 있는가에 대한 함수
    if x < 0 or y < 0 or x >= N or y >= M: return False
    elif visit[x][y] == INF: return False
    elif garden[x][y] == 0: return False
    return True

S = [0 for _ in range(G + R)]
for pos in combinations(broth, G + R): # 조합으로 배양액을 뿌릴 수 있는 땅 선택해서
    select(S, 0, pos, G, R) # bfs로 정답 갱신

print(ans) # 최대값 출력