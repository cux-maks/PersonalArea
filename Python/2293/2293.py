N, K = map(int, input().split())
coin = [int(input()) for _ in range(N)]
coin.sort()
dp = [0 for _ in range(K + 1)]
dp[0] = 1
for i in coin:
    for j in range(i, K + 1):
        if j >= i: dp[j] += dp[j - i]
    
print(dp[K])