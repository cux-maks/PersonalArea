import sys
input = sys.stdin.readline

S = list(input().rstrip())
if S == list(reversed(S)): print(1)
else: print(0)