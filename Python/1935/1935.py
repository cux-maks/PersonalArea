import sys
input = sys.stdin.readline

N = int(input())
S = list(input().rstrip())
stack = []
val = {}

for i in range(N):
    val[chr(i + 65)] = int(input())

for i in S:
    if 'A' <= i <= 'Z': stack.append(val[i])
    else:
        a, b = stack.pop(), stack.pop()
        if i == '+': stack.append(a + b)
        elif i == '-': stack.append(b - a)
        elif i == '*': stack.append(a * b)
        elif i == '/': stack.append(b / a)

print('{0:.2f}'.format(stack[0]))