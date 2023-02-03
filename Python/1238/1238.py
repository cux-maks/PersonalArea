import heapq
import sys
input = sys.stdin.readline

N, M, X = map(int, input().rstrip().split())

graph = {}

for i in range(M):
    a, b, c = map(int, input().rstrip().split())
    if a not in graph: graph[a] = {}
    graph[a][b] = c

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

go = {i:dijkstra(i)[X] for i in range(1, N + 1)}
back = {i:dijkstra(X)[i] for i in range(1, N + 1)}
result = 0
for i in range(1, N + 1):
    result = max(result, go[i] + back[i])
print(result)