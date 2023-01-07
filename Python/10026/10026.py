from collections import deque # bfs를 위한 deque import
import sys # input함수 재정의를 위해 sys import

input = sys.stdin.readline # input함수 재정의

N = int(input()) # N 입력
paint = [list(input()) for _ in range(N)] # 그림 입력
visited = [[False for _ in range(N)] for _ in range(N)] # bfs함수를 위한 visited리스트 생성

dx = [1, -1, 0, 0] # dx 선언 - 2차원리스트에서 x의 변화량 담당
dy = [0, 0, 1, -1] # dy 선언 - 2차원리스트에서 y의 변화량 담당



def bfs(i, j, c): # bfs함수 선언
    q = deque([]) # deque 생성
    q.append([i, j, c]) # deque에 시작 좌표 (i, j)와 색상 (c)를 추가
    while q: # q에 원소가 존재할 경우 반복
        x, y, color = q.popleft() # q의 원소중 가장 왼쪽 원소를 pop
        for i in range(4): # 4번 반복
            nx = x + dx[i] # nx구하기
            ny = y + dy[i] # ny구하기
            if 0 <= nx < N and 0 <= ny < N and (not visited[nx][ny]) and paint[nx][ny] == color: # nx, ny에 방문한 적 없고, 이전 색상과 같을 경우
                visited[nx][ny] = True # 방문 여부를 True로 변경
                q.append([nx, ny, color]) # q에 해당 좌표와 색상 추가

not_cnt = 0 # 적록색약이 아닌 경우 카운트 생성
yes_cnt = 0 # 적록색양인 경우 카운트 생성

for i in range(N): # N번 반복
    for j in range(N): # N번 반복
       if not visited[i][j]: # 만약 방문한 적 없는 곳이라면
        bfs(i, j, paint[i][j]) # bfs함수 호출
        not_cnt += 1 # 적록색약이 아닌 경우 구역 카운트 1 증가

for i in range(N): # N번 반복
    for j in range(N): # N번 반복
        if paint[i][j] == 'G': paint[i][j] = 'R' # 적록색약이기 때문에 모든 G를 R로 바꾼다. (R을 G로 바꿔도 상관 없다)
        visited[i][j] = False # 모든 방문여부를 초기화한다

for i in range(N): # N번 반복
    for j in range(N): # N번 반복
        if not visited[i][j]: # 만약 방문한 적 없는 곳이라면
            bfs(i, j, paint[i][j]) # bfs함수 호출
            yes_cnt += 1 # 적록색약인 경우 구역 카운트 1 증가

print(not_cnt, yes_cnt) # 카운트 출력