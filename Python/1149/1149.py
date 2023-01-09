import sys
input = sys.stdin.readline

N = int(input())
price = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    price[i][0] = min(price[i - 1][1], price[i - 1][2]) + price[i][0]
    price[i][1] = min(price[i - 1][0], price[i - 1][2]) + price[i][1]
    price[i][2] = min(price[i - 1][0], price[i - 1][1]) + price[i][2]
    
print(min(price[N - 1]))