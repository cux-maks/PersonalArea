N, B = input().split(" ")
B = int(B)
N = ''.join(reversed(N))
number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = 0
for i in range(len(N) - 1, -1, -1):
    result += number.index(N[i]) * (B**i)
print(result)