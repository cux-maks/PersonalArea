N, M = map(int, input().split())
b = [i + 1 for i in range(N + 1)]
for _ in range(M):
    i, j = map(int, input().split())
    print(b[0:i - 1])
    print(b[i - 1:j:-1])
    print(b[j:])
    # b = b[:i] + b[i:j:-1] + b[j + 1:]
    # print(b)
print(*b)