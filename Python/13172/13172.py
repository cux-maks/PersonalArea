import sys
import math
input = sys.stdin.readline

FLAG = 1000000007
sum = 0
M = int(input())

def power(a, n):
    if n == 0: return 1
    x = power(a, n // 2) % FLAG
    if n % 2 == 0: return x * x % FLAG
    else: return x * x * a % FLAG

for i in range(M):
    n, s = map(int,input().rstrip().split())
    a = s // math.gcd(n, s)
    b = n // math.gcd(n, s)

    b_inverse = power(b, FLAG-2) % FLAG
    sum += (a * b_inverse) % FLAG
    sum %= FLAG

print(sum)