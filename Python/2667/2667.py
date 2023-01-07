from collections import deque # bfs에 사용할 deque import

N = int(input()) # N입력
apt = [[int(x) for x in list(input())] for _ in range(N)] # 아파트 입력

dx = [1, -1, 0, 0] # x 변화량 선언
dy = [0, 0, 1, -1] # y 변화량 선언

def bfs(i, j): #bfs함수 정의
    global apt
    q = deque()
    q.append([i, j])
    apt[i][j] = 0
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and apt[nx][ny] == 1:
                apt[nx][ny] = 0
                q.append([nx, ny])
                cnt += 1 # 가구수 1씩 증가
    return cnt # 해당 동의 가구수 반환

house = []

for i in range(N):
    for j in range(N):
        if apt[i][j] == 1:
            house.append(bfs(i, j)) # 반환값을 결과값 리스트에 추가

print(len(house)) # 결과값 리스트의 원소 개수 출력
house.sort() # 정렬
for i in house: print(i) # 정렬된 원소를 하나씩 출력