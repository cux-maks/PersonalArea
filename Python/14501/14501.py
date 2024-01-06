import sys
input = sys.stdin.readline

N = int(input().rstrip())
schedule = [[None for _ in range(N)] for _ in range(2)]
dp = [0 for _ in range(N)]

for i in range(N):
    schedule[0][i], schedule[1][i] = map(int, input().rstrip().split())

for i in range(N):
    possible = []
    for j in range(i):
        if schedule[0][j] + j <= i:
            possible.append(dp[j])
    if len(possible) == 0:
        if schedule[0][i] + i <= N:
            dp[i] = schedule[1][i]
        else:
            dp[i] = max(dp)
    else:
        if schedule[0][i] + i <= N:
            dp[i] = schedule[1][i] + max(possible)
        else:
            dp[i] = max(possible)
        
print(max(dp))