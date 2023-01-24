import sys
input = sys.stdin.readline

N = int(input())
for i in range(1, N + 1):
    S = list(input().rstrip().split(' '))
    print(f"Case #{i}: ", end = '')
    while S: print(S.pop(), end = ' ')
    print()