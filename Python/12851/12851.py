from collections import deque, defaultdict

N, K = map(int, input().split())
res = defaultdict(int)
visited = [False for _ in range(100001)]
q = deque()
q.append([N, 0])

while q:
    x, cnt = q.popleft()
    visited[x] = True
    if x == K: res[cnt] += 1
    else:
        for i in [x * 2, x + 1, x - 1]:
            if 0 <= i < 100001 and not visited[i]:
                q.append([i, cnt + 1])

for key in res.keys():
    print(key)
    print(res[key])
    break