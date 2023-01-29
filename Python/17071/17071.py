import sys
input = sys.stdin.readline

MAX = 500001
N, K = map(int, input().rstrip().split())

def possible(x):
    return 0 <= x < MAX

visited = [[-1 for _ in range(2)] for _ in range(MAX)]
if N == K: print(0)
else:
    q = [N]
    t = 1
    K += 1
    while True:
        if K >= MAX:
            print(-1)
            break
        buf = []
        for x in q:
            for nx in [x + 1, x - 1, x * 2]:
                if possible(nx) and visited[nx][t % 2] == -1:
                    buf.append(nx)
                    visited[nx][t % 2] = t
        if visited[K][t % 2] != -1:
            print(t)
            break
        t += 1
        K += t
        q = buf