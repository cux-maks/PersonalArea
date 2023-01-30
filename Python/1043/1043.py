import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
R = set(map(int, input().rstrip().split()[1:]))
party = [set(map(int, input().rstrip().split()[1:])) for _ in range(M)]

for _ in range(M):
    for x in party:
        if x & R:
            R = R.union(x)

result = 0
for x in party:
    if x & R: continue
    result += 1

print(result)