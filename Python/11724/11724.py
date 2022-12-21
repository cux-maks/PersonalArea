import sys # 재귀호출 깊이 설정과 input함수 재정의를 위해 import

sys.setrecursionlimit(5000) # boj서버에는 이 값이 1000으로 설정되어있어서 이 문제를 해결하기에 부족함. 따라서 5000으로 증가.
input = sys.stdin.readline # input함수를 sys.stdin.readline으로 하여 기본 input함수보다 더 빠르게 처리 가능

N, M = map(int, input().split()) # N과 M을 입력받음

visited = [False for _ in range(N + 1)] # visited리스트를 전부 False로 생성
graph = list(list() for _ in range(N + 1)) # 그래프 생성
cnt = 0 # 결과값 cnt 0으로 설정

def dfs(start): # dfs함수 정의
    visited[start] = True # start부분의 visited를 True로 설정
    for i in graph[start]: # graph[start]에 있는 원소를 하나씩 불러와서
        if not visited[i]: # 만약에 i가 False(방문한 적 없다)면, 
            dfs(i) # i를 start로 하여 dfs 호출(재귀)

for _ in range(M): # M만큼 반복하여
    u, v = map(int, input().split()) # 간선의 양 끝점 u, v를 입력받는다.
    graph[u].append(v) # graph[u]에 v값 추가
    graph[v].append(u) # graph[v]에 u값 추가

for i in range(1, N + 1): # 1부터 N + 1까지 만큼 반복하여
    if not visited[i]: # 만약 i에 방문한 적이 없다면
        dfs(i) # i를 start로 하여 dfs 호출
        cnt += 1 # 카운트 += 1
        # dfs를 호출하고 카운트를 증가시키는 이유?
        # dfs를 호출하면 연결된 모든 원소의 visited값을 True로 바꿔준다.
        # 연결된 모든 원소를 지났기 때문에 하나의 연결요소를 탐색했다고 판단하여 cnt += 1 해준다.
        # for 반복문을 진행하면서 만약 visited값이 False인 원소가 나온다면? 다시 dfs를 호출하고 cnt += 1을 해준다.
        # dfs가 호출된 수 만큼이 주어진 그래프의 연결요소의 개수가 된다.

print(cnt) # 연결요소 개수 출력