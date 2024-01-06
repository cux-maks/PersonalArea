import sys
input = sys.stdin.readline

def pop(stack: list):
    if len(stack) == 0:
        print(-1)
    else: 
        print(stack[-1])
        stack.pop()

def count(stack: list):
    print(len(stack))

def empty(stack: list):
    if len(stack) == 0: print(1)
    else: print(0)

def top(stack: list):
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])

stack = []
command = {
    2: pop, 3: count, 4: empty, 5: top
}

for _ in range(int(input().rstrip())):
    func = list(map(int, input().rstrip().split()))
    if len(func) == 2:
        stack.append(func[1])
    else:
        command[func[0]](stack)