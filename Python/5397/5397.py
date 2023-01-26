import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    S = list(input().rstrip())
    stack_L = []
    stack_R = []
    for i in range(len(S)):
        if S[i] == '-':
            if stack_L: stack_L.pop()
        elif S[i] == '<':
            if stack_L: stack_R.append(stack_L.pop())
        elif S[i] == '>':
            if stack_R: stack_L.append(stack_R.pop())
        else: stack_L.append(S[i])
    stack_L.extend(reversed(stack_R))
    print(''.join(stack_L))