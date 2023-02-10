from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
q = deque([i for i in range(1, N + 1)])
result = []
idx = 1

while q:
    for _ in range(K -1):
        q.append(q.popleft())
    result.append(q.popleft())

print(str(result).replace('[', '<').replace(']', '>'))