from collections import deque
import sys; input = sys.stdin.readline

N, M, K = map(int, input().split()) # N, M, K 입력
grid = [input().rstrip() for _ in range(N)] # 그리드 입력
visited = [[[0 for _ in range(K + 1)] for _ in range(M)] for _ in range(N)]
visited[0][0] = [1 for _ in range(K + 1)]
d = ((1, 0), (-1, 0), (0, 1), (0, -1))

def able(a, b, c): # 방문 가능한지 확인하는 함수
    return 0 <= a < N and 0 <= b < M and not visited[a][b][c]

def bfs(): # bfs
    q = deque([])
    q.append((0, 0, 0))
    ans = 1
    while q:
        night = False if ans > 0 else True # 낮인지 밤인지 판별
        for _ in range(len(q)): # q에 들어있는 원소의 개수만큼만 반복
            x, y, z = q.popleft()
            if x == N - 1 and y == M - 1: return abs(ans) # 만일 도착했다면 결과값 반환
            for dx, dy in d: # 
                nx, ny = x + dx, y + dy # 상하좌우 이동
                if able(nx, ny, z): # 이동가능하면
                    if grid[nx][ny] == '0': # 만약 0이면 -> 낮이든 밤이든 상관 없이 이동 가능
                        visited[nx][ny][z] = ans + 1 # 방문 여부를 현재 일수 + 1로 설정
                        q.append((nx, ny, z)) # q에 추가
                    elif z < K and not visited[nx][ny][z + 1]: # 만약 벽이고, 방문한 적 없다면
                        if not night: # 밤이 아니라면
                            visited[nx][ny][z + 1] = ans + 1 # 방문 여부를 현재 일수 + 1로 설정
                            q.append((nx, ny, z + 1)) # q에 추가
                        else: # 밤이라면
                            q.append((x, y, z)) # 제자리 추가
        ans = ans + 1 if ans > 0 else ans - 1 # 결과값 1 증가
        ans *= -1 # 음수 변경 -> 음수 여부로 낮인지 밤인지 판별
    return -1

print(bfs())