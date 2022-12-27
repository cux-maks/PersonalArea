from collections import deque # deque 사용을 위해 import

M, N = map(int, input().split()) # map 크기 입력
box = [list(map(int, input().split())) for _ in range(N)] # box입력
a, b = None, None # 익은 토마토의 좌표를 저장하기 위해 a, b를 None으로 선언
dx = [-1, 1, 0, 0] # x 변화량 리스트 생성
dy = [0, 0, -1, 1] # y 변화량 리스트 생성
result = 0 # 결과값 저장 위한 result 생성
q = deque([]) # bfs함수를 위한 deque 생성

for i in range(N): # 
    for j in range(M): # 
        if box[i][j] == 1: q.append([i, j]) # box를 하나하나 탐색해서 1인 지점의 좌표 deque에 추가


def sol(): # bfs함수

    while q:
        
        x, y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < N and 0 <= ny < M and box[nx][ny] == 0: # 만약 box의 범위를 벗어나지 않고, 해당 인덱스의 값이 0이라면
                box[nx][ny] = box[x][y] + 1 # 해당 인덱스 값을 x, y인덱스값 + 1로 바꿔줌
                q.append([nx, ny])

sol() # bfs탐색 종료 후 box의 원소중 가장 큰 값 - 1이 걸린 시간일것임

for i in box: # box의 리스트를 하나씩 가져오고
    if 0 in i: # 그 리스트 안에 0이 존재한다면
        print(-1) # -1을 출력
        exit(0) # 하고 프로그램 종료
    result = max(max(i), result) # 반복문을 진행하면서, result에는 최대값을 계속 갱신해줌

print(result - 1) # result - 1을 출력하여 시간 출력