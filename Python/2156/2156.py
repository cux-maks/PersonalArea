import sys
input = sys.stdin.readline

N = int(input())
num = [int(input()) for _ in range(N)]
dp = [0 for _ in range(10000)]
dp[0] = num[0]
if N > 1: dp[1] = num[0] + num[1]
if N > 2: dp[2] = max(num[0] + num[2], num[1] + num[2], num[0] + num[1])
for i in range(3, N):
    dp[i] = max(num[i] + dp[i - 2], num[i] + num[i - 1] + dp[i - 3], dp[i - 1])
print(max(dp))