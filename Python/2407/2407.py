n, m = map(int, input().split())
a, b = 1, 1
for i in range(n, n - m, -1): a *= i
for i in range(1, m + 1, 1): b *= i
print(a // b)