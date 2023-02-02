N = sorted([int(input()) for _ in range(9)])
ans = sum(N)
x, y = int(), int()
for i in range(9):
    for j in range(9):
        if i != j and ans - N[i] - N[j] == 100:
            x, y = i, j
            break
for i in range(9):
    if i != x and i != y: print(N[i])