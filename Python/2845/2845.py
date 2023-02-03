L, P = map(int, input().split())
num = list(map(int, input().split()))
for i in range(len(num)):
    num[i] = num[i] - (L * P)
print(*num)