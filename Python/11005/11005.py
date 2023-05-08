N, B = map(int, input().split(" "))
number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = ""
while N != 0:
    a = N % B
    N = N // B
    result += number[a]

print("".join(reversed(result)))