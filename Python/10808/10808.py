import sys
input = sys.stdin.readline

res = [0 for _ in range(26)]
for x in list(input().rstrip()): res[ord(x) - 97] += 1
print(*res)