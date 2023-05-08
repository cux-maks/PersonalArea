N = int(input())
nums = list()

for _ in range(N):
    a = int(input())
    nums.append(a)

dp = [0, 1, 2, 4]
for i in range(4, max(nums) + 1):
    dp.append((dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1000000009)

for a in nums: print(dp[a])