import sys
input = sys.stdin.readline

N = int(input().rstrip())
for i in range(N - 1):
    space = (N - 1 - i) * " "
    star = ((i * 2) + 1) * "*"
    print(f"{space}{star}")
for i in range(N - 1, -1, -1):
    space = (N - 1 - i) * " "
    star = ((i * 2) + 1) * "*"
    print(f"{space}{star}")
