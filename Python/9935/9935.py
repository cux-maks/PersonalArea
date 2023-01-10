s = input()
pattern = input()

L = len(pattern)
stack = []

for x in s:
    stack.append(x)
    if x == pattern[-1] and ''.join(stack[-L:]) == pattern:
        del stack[-L:]

s = ''.join(stack)
if s == '': print("FRULA")
else: print(s)