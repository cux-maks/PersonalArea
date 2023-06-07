import sys
input = sys.stdin.readline

for _ in range(3):
    S = sum(list(map(int, input().rstrip().split())))
    if S == 1: print('C')
    elif S == 2: print('B')
    elif S == 3: print('A')
    elif S == 0: print('D')
    elif S == 4: print('E')