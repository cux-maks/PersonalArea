H, M, S = map(int, input().split())
time = int(input())
S += time
M += S // 60
S %= 60
H += M // 60
M %= 60
H %= 24
print(f"{H} {M} {S}")