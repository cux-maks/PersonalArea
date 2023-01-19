from collections import deque

X = int(input())

cnt = [0 for _ in range(X + 1)]
visit = [False for _ in range(X + 1)]

def bfs():
    q = deque([])
    q.append([X, [X]])
    visit[X] = True
    while q:
        a, way = q.popleft()
        if a == 1: break
        if a % 3 == 0 and not visit[a // 3]:
            q.append([a // 3, way + [a // 3]])
            visit[a // 3] = True
            cnt[a // 3] = cnt[a] + 1
        if a % 2 == 0 and not visit[a // 2]:
            q.append([a // 2, way + [a // 2]])
            visit[a // 2] = True
            cnt[a // 2] = cnt[a] + 1
        if a - 1 > 0 and not visit[a - 1]:
            q.append([a - 1, way + [a - 1]])
            visit[a - 1] = True
            cnt[a - 1] = cnt[a] + 1
    print(cnt[1])
    for x in way: print(x, end = ' ')

bfs()