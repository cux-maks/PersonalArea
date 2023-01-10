from collections import deque
import sys

input = sys.stdin.readline

N, K = map(int, input().split())

def bfs():

    q = deque()
    q.append(N)
    visited = [-1 for _ in range(100001)]
    visited[N] = 0

    while q:
        x = q.popleft()
        if x == K: 
            return visited[x]
        for i in [x * 2, x + 1, x - 1]:
            if 0 <= i < 100001 and visited[i] == -1:
                if i == x * 2:
                    visited[i] = visited[x]
                    q.appendleft(i)
                else:
                    visited[i] = visited[x] + 1
                    q.append(i)

print(bfs())