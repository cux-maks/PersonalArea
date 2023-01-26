import sys
input = sys.stdin.readline
N = int(input())
cnt = 0
for _ in range(N):
    S = list(input().rstrip())
    stack = []
    for x in S:
        if stack and x == stack[-1]: stack.pop()
        else: stack.append(x)
    if not stack: cnt += 1
print(cnt)