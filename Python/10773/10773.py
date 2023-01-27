import sys
input = sys.stdin.readline

K = int(input())
result = []

for _ in range(K):
    a = int(input())
    if a == 0: result.pop()
    else: result.append(a)

print(sum(result))