N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
chicken = []
house = []
for i in range(N):
    for j in range(N):
        if grid[i][j] == 2: chicken.append((i, j))
        elif grid[i][j] == 1: house.append((i, j))

ans = N * N * N

def backTracking(start, c):
    global ans
    if len(c) == M:
        result = 0
        for x in house:
            buf = N * N
            for a in c:
                dist = abs(a[0] - x[0]) + abs(a[1] - x[1])
                buf = min(dist, buf)
            result += buf
        ans = min(ans, result)
    for i in range(start, len(chicken)):
        if chicken[i] not in c:
            c.append(chicken[i])
            backTracking(i, c)
            c.pop()

backTracking(0, [])

print(ans)