from collections import deque # deque 사용을 위해 import

cnt = [0] * 100001 # 미리 100000개의 인덱스 생성해두기

def sol(n): # bfs함수
    q = deque([n]) # deque에 n대입
    while q: # q가 비어있지 않다면
        n = q.popleft() # n = q의 왼쪽에서 원소 pop하여 대입
        if n == K: return cnt[n] # 만약 n == K라면 cnt리스트의 n번째 인덱스 값 전달
        for i in (n - 1, n + 1, 2 * n): # 튜플의 값 n - 1, n + 1, n * 2를 하나씩 가져와
            if 0 <= i < 100001 and not cnt[i]: # 만약 cnt[i]가 0이고, i의 값이 0 ~ 100000사이라면
                cnt[i] = cnt[n] + 1 # cnt[i]의 값은 cnt[n] + 1이다. (방문 번째 횟수: 그러니까 i번째 인덱스를 몇 번째로 방문했는지)
                q.append(i) # q에 i대입

N, K = map(int, input().split()) # N, K입력

result = sol(N) # bfs결과를 result에 대입
print(result) # result 출력