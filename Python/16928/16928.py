from collections import deque # bfs함수를 위한 deque import
import sys # input함수 재정의를 위한 sys import
input = sys.stdin.readline # input함수 재정의

N, M = map(int, input().split()) # N, M 입력

grid = [i for i in range(101)] # grid생성 - 해당 인덱스에 도착했을 때, 이동하게되는 칸을 나타냄.
# ex) grid[32] = 32라면, 32번 칸에 도달했을 때 32번칸에 있는다는 뜻.
# ex) grid[28] = 99라면, 28번 칸에 도달했을 때, 99번칸으로 간다는 뜻.
visited = [False for _ in range(101)] # 방문 여부 리스트 생성

for _ in range(N + M): # 사다리의 개수 + 뱀의 개수 만큼 반복
    a, b = map(int, input().split()) # 시작점과 끝점 입력
    grid[a] = b # grid의 a번째 인덱스의 값을 b로 변경

def bfs(): # bfs함수 정의
    q = deque()
    q.append([1, 0]) # 시작점과 주사위를 던진 횟수를 q에 추가
    while q: # q가 비어있지 않다면 계속해서 반복
        now, cnt = q.popleft() # q에서 가장 왼쪽 원소 pop
        if now == 100: return cnt # 만약 현재 칸의 번호가 100이라면 주사위를 던진 횟수를 반환
        for i in range(1, 7): # 1 ~ 6까지 반복하여
            if 0 <= now + i < 101 and not visited[now + i]: # 만약 현재 위치에서 주사위 눈 만큼 이동한 것이 100이하이고, 해당 칸에 방문한 적이 없다면
                visited[now + i] = True # 방문 여부를 True로 변경하고
                q.append([grid[now + i], cnt + 1]) # 해당 칸을 인덱스로 하여 grid[now + i]와 주사위 던진횟수를 q에 추가한다.

print(bfs()) # 리턴값을 출력한다.