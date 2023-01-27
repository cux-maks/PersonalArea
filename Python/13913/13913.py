from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
visited = [-1 for _ in range(100001)]
q = deque([])
q.append((N, 0))
visited[N] = N
result = []
while q:
    x, time = q.popleft()
    if x == K:
        idx = x
        while idx != N:
            result.append(idx)
            idx = visited[idx]
        result.append(N)
        print(time)
        print(*result[::-1])
        break
    nx = x + 1
    if 0 <= nx < 100001 and visited[nx] == -1:
        visited[nx] = x
        q.append((nx, time + 1))

    nx = x - 1
    if 0 <= nx < 100001 and visited[nx] == -1:
        visited[nx] = x
        q.append((nx, time + 1))

    nx = 2 * x
    if 0 <= nx < 100001 and visited[nx] == -1:
        visited[nx] = x
        q.append((nx, time + 1))
