N = int(input())
dp = [0 for _ in range(N + 1)]
dp[1] = 0
for i in range(2, N + 1):
    dp[i] = dp[i - 1] + 1
    if not i % 3: dp[i] = min(dp[i], dp[i//3] + 1)
    if not i % 2: dp[i] = min(dp[i], dp[i//2] + 1)

print(dp[N])