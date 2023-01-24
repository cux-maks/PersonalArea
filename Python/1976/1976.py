import sys;
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

N = int(input())
M = int(input())

city = [i for i in range(N + 1)]

def find(x):
    if city[x] != x:
        city[x] = find(city[x])
    return city[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b: city[b] = a
    else: city[a] = b

for i in range(N):
    root = list(map(int, input().rstrip().split()))
    for j in range(N):
        if root[j] == 1: union(i + 1, j + 1)

trip = list(map(int, input().rstrip().split()))
result = find(trip[0])
for i in range(1, len(trip)):
    if result != find(trip[i]):
        result = 0
        break

if result: print("YES")
else: print("NO")