MIN, MAX = map(int, input().split())
result = [1] * (MAX - MIN + 1)
num = [i**2 for i in range(2, int(MAX**(1/2) + 1))]

for i in num:
    n = MIN // i * i
    while(n < MAX + 1):
        if n - MIN >= 0: result[n - MIN] = 0
        n += i

print(sum(result))