N = int(input())
A = list(map(int, input().split()))

X = dict()
for i, num in enumerate(A): X[num] = i

A.sort()

Y = dict()
for i, num in enumerate(A): Y[num] = i

ans = 0
for num in X:
    buf = X[num] - Y[num]
    if buf > 0 and buf > ans: ans = buf

print(ans)