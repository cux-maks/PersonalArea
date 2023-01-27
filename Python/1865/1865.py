import sys
input = sys.stdin.readline

T = int(input())

def bf():
    for i in range(N):
        for j in range(len(road)):
            a, b, c = road[j]
            if distance[b] > distance[a] + c:
                distance[b] = distance[a] + c
                if i == N - 1:
                    return True
    return False

for _ in range(T):
    N, M, W = map(int, input().rstrip().split())
    road = []
    distance = [1e9 for _ in range(N + 1)]
    for i in range(M):
        s, e, t = map(int, input().rstrip().split())
        road.append((e, s, t))
        road.append((s, e, t))
    for i in range(W):
        s, e, t = map(int, input().rstrip().split())
        road.append((s, e, -t))
    print(distance)
    print(road)
    if bf(): print("YES")
    else: print("NO")
    print(distance)
    print(road)
