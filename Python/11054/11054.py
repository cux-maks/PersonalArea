N = int(input())
num = list(map(int, input().split()))
reverse_num = num[::-1]
dp_up = [1 for _ in range(N)]
dp_down = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if num[i] > num[j]: dp_up[i] = max(dp_up[i], dp_up[j] + 1)
        if reverse_num[i] > reverse_num[j]: dp_down[i] = max(dp_down[i], dp_down[j] + 1)

ans = 0

for i in range(N):
    ans = max(dp_up[i] + dp_down[N - i - 1], ans)

print(ans - 1)