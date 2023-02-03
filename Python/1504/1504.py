import heapq
import sys

input = sys.stdin.readline

N, E = map(int, input().rstrip().split())

graph = {}
for i in range(1, N + 1): graph[i] = {}

for _ in range(E):
    a, b, c = map(int, input().rstrip().split())
    if a not in graph: graph[a] = {}
    if b not in graph: graph[b] = {}
    graph[a][b] = c
    graph[b][a] = c

v1, v2 = map(int, input().rstrip().split())

def dijkstra(start):

    distances = {node: sys.maxsize for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, (distances[start], start))

    while queue:
        current_distance, node = heapq.heappop(queue)
        if distances[node] < current_distance:
            continue
        for adjacency_node, distance in graph[node].items():
            weighted_distance = current_distance + distance
            if weighted_distance < distances[adjacency_node]:
                distances[adjacency_node] = weighted_distance
                heapq.heappush(queue, (weighted_distance, adjacency_node))

    return distances

one = dijkstra(1)
v1_ = dijkstra(v1)
v2_ = dijkstra(v2)
result = min(one[v1] + v1_[v2] + v2_[N], one[v2] + v2_[v1] + v1_[N])
print(result if result < sys.maxsize else -1)
