import sys
from collections import deque

input = sys.stdin.readline

dq = deque([])

N = int(input().rstrip())
nums = list(map(int, input().rstrip().split()))
res = []

for i in range(1, N + 1):
    dq.append((i, nums[i - 1]))

while dq:
    i, k = dq.popleft()
    if dq and k > 0:
        for j in range(k - 1):
            dq.append(dq.popleft())
    elif dq and k < 0:
        for j in range(k * (-1)):
            dq.appendleft(dq.pop())
    else:
        res.append(i)
        break
    res.append(i)

print(*res)