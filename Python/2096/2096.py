N = int(input())
max_dp = [0, 0, 0]
min_dp = [0, 0, 0]
max_buf = [0, 0, 0]
min_buf = [0, 0, 0]

for i in range(N):

    a, b, c = map(int, input().split())

    max_buf[0] = a + max(max_dp[0], max_dp[1])
    max_buf[1] = b + max(max_dp[0], max_dp[1], max_dp[2])
    max_buf[2] = c + max(max_dp[1], max_dp[2])

    min_buf[0] = a + min(min_dp[0], min_dp[1])
    min_buf[1] = b + min(min_dp[0], min_dp[1], min_dp[2])
    min_buf[2] = c + min(min_dp[1], min_dp[2])

    max_dp[0] = max_buf[0]
    max_dp[1] = max_buf[1]
    max_dp[2] = max_buf[2]

    min_dp[0] = min_buf[0]
    min_dp[1] = min_buf[1]
    min_dp[2] = min_buf[2]

print(max(max_dp), min(min_dp))