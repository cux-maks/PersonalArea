from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = defaultdict(list)
for i in range(M):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b, c))

start, end = map(int, input().rstrip().split())

prev_node = [0 for _ in range(N + 1)]

def dijkstra(start):

    distances = [sys.maxsize for _ in range(N + 1)]
    distances[start] = 0
    queue = []
    heapq.heappush(queue, (distances[start], start))

    while queue:
        current_distance, node = heapq.heappop(queue)
        if distances[node] < current_distance:
            continue
        for adjacency_node, distance in graph[node]:
            weighted_distance = current_distance + distance
            if weighted_distance < distances[adjacency_node]:
                distances[adjacency_node] = weighted_distance
                prev_node[adjacency_node] = node
                heapq.heappush(queue, (weighted_distance, adjacency_node))

    return distances

print(dijkstra(start)[end])
path = [end]
now = end
while now != start:
    now = prev_node[now]
    path.append(now)
path.reverse()
print(len(path))
print(*path)