N, M = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
visited = [False for _ in range(N)]
buf = []
result = set()

def BT(start):
    if len(buf) == M:
        result.add(tuple(buf))
        return
    for i in range(N):
        if visited[i]:
            continue
        buf.append(num[i])
        visited[i] = True
        BT(start + 1)
        visited[i] = False
        buf.pop()

BT(-1)
result = list(result)
result.sort()
for x in result: print(*x)