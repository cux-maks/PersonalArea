import sys
input = sys.stdin.readline

MAX = 10 ** 9

def cal(command, n):

    stack = [n]

    for x in command:
        if "NUM" in x:
            stack.append(int(x.split()[1]))
        elif stack and x == "POP":
            stack.pop()
        elif stack and x == "INV":
            stack[-1] = -1 * stack[-1]
        elif stack and x == "DUP":
            stack.append(stack[-1])
        elif len(stack) > 1 and x == "SWP":
            a = stack.pop()
            b = stack.pop()
            stack.append(a)
            stack.append(b)
        elif len(stack) > 1 and x == "ADD":
            a = stack.pop()
            b = stack.pop()
            c = b + a
            if abs(c) > MAX:
                 return "ERROR"
            stack.append(c)
        elif len(stack) > 1 and x == "SUB":
            a = stack.pop()
            b = stack.pop()
            c = b - a
            if abs(c) > MAX:
                return "ERROR"
            stack.append(c)
        elif len(stack) > 1 and x == "MUL":
            a = stack.pop()
            b = stack.pop()
            c = b * a
            if abs(c) > MAX:
                return "ERROR"
            stack.append(c)
        elif len(stack) > 1 and x == "DIV":
            a = stack.pop()
            b = stack.pop()
            if a == 0:
                return "ERROR"
            c = abs(b) // abs(a)
            if a * b < 0: c = -1 * c
            if abs(c) > MAX:
                return "ERROR"
            stack.append(c)
        elif len(stack) > 1 and x == "MOD":
            a = stack.pop()
            b = stack.pop()
            if a == 0:
                return "ERROR"
            c = abs(b) % abs(a)
            if b < 0: c = -1 * c
            if abs(c) > MAX:
                return "ERROR"
            stack.append(c)
        else:
            return "ERROR"
    if len(stack) == 1: return stack.pop()
    else: return "ERROR"

while True:
    cmd = []
    while True:
        w = input().rstrip()
        if w == "END": break
        if w == "QUIT": quit()
        cmd.append(w)
    N = int(input())
    for _ in range(N):
        i = int(input())
        print(cal(cmd, i))
    print()
    input()