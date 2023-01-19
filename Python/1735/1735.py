import math

a, b = map(int, input().split())
c, d = map(int, input().split())
x = b * d
y = b * c + d * a
k = math.gcd(x, y)
x = x // k
y = y // k
print(y, x)