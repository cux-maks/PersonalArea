import sys; input = sys.stdin.readline

N, K = map(int, input().split())
temp = list(map(int, input().split()))
window = sum(temp[:K])
result = window
for i in range(K, N):
    window += temp[i] - temp[i - K]
    result = max(result, window)
print(result)