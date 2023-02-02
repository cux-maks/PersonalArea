N = int(input())
A = sorted([int(input()) for _ in range(N)], reverse = True)
B = [0 for _ in range(N)]

for i in range(N, 0, -1):
    B[i - 1] = A[i - 1] * i

print(max(B))