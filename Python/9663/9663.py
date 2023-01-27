N = int(input())
grid = [0 for _ in range(N)]
result = 0

def promising(x):
    for i in range(x):
        if grid[x] == grid[i] or abs(grid[x] - grid[i]) == abs(x - i):
            return False
    return True

def NQeen(x):
    global result
    if x == N:
        result += 1
        return
    else:
        for i in range(N):
            grid[x] = i
            if promising(x): NQeen(x + 1)

NQeen(0)
print(result)