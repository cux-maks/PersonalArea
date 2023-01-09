import sys
input = sys.stdin.readline

N = int(input())
num = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    for j in range(len(num[i])):
        if j == 0:
            num[i][j] += num[i - 1][j]
        elif j == len(num[i]) - 1:
            num[i][j] += num[i - 1][j - 1]
        else:
            num[i][j] += max(num[i - 1][j], num[i - 1][j - 1])
        
print(max(num[N - 1]))