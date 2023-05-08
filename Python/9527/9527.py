import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

def sum_f(x):
    if x <= 0:
        return 0

    s = int(math.log2(x))
    f = 2 ** s
    if f == x:
        return s * x // 2 + 1

    d = x - f
    return sum_f(f) + d + sum_f(d)

a, b = map(int, input().rstrip().split())
print(sum_f(b) - sum_f(a - 1))