import sys
input = sys.stdin.readline

N = int(input())
S = list(input().rstrip())
cnt = 1
i = 0
while i < len(S):
    if S[i] == 'S':
        i += 1
    elif S[i] == 'L':
        i += 2
    cnt += 1
print(min(N, cnt))