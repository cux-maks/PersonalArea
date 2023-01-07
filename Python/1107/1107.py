buttons = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

N = int(input())
M = int(input())

broken = []
if M != 0: broken = list(map(int, input().split()))

cnt = abs(100 - N)

for x in range(1000001):
    num = str(x)
    for i in range(len(num)):
        if int(num[i]) in broken:
            break
        if i == len(num) - 1:
            cnt = min(cnt, abs(N - x) + len(num))

print(cnt)