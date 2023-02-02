import heapq
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

N = int(input())
M = int(input())
tree = [[] for _ in range(N + 1)]

for _ in range(M):
    p, c, v = map(int, input().rstrip().split())
    tree[p].append((c, v))

start, end = map(int, input().split())

def dijkstra(start):
    dist = [[float('inf'), []] for i in range(N + 1)]
    dist[start][0] = 0
    dist[start][1] = [start]
    q = []
    heapq.heappush(q, [dist[start][0], start])

    while q:
        d, now = heapq.heappop(q)
        if dist[now][0] < d: continue
        for i in tree[now]:
            if d + i[1] < dist[i[0]][0]:
                dist[i[0]][0] = d + i[1]
                dist[i[0]][1].append(now)
                heapq.heappush(q, (dist[i[0]][0], i[0]))
    
    return dist

print(tree)
print(dijkstra(start)[end])