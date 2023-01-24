import sys
input = sys.stdin.readline

S1 = list(input().rstrip())
S2 = []
N = int(input())
curr = len(S1)

for _ in range(N):
    cmd = list(input().rstrip().split(' '))
    if cmd[0] == 'P':
        S1.append(str(cmd[1]))
    elif cmd[0] == 'L':
        if S1: S2.append(S1.pop())
    elif cmd[0] == 'D':
        if S2: S1.append(S2.pop())
    elif cmd[0] == 'B':
        if S1: S1.pop()

S1.extend(reversed(S2))
print(''.join(S1))