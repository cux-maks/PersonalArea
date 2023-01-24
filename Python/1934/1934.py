from math import lcm
N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    print(lcm(a, b))