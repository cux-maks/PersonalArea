import sys
input = sys.stdin.readline

N = int(input())
position = [list(map(int, input().rstrip().split())) for _ in range(N)]
position.append(position[0])
buf_1 = 0
buf_2 = 0

for i in range(N):
    buf_1 += position[i][0] * position[i + 1][1]
    buf_2 += position[i][1] * position[i + 1][0]

ans = round((buf_1 - buf_2) / 2, 1)
if ans < 0: ans *= -1
print(ans)