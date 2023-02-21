import sys; input = sys.stdin.readline

grid = [list(map(lambda x: int(x), list(input().rstrip()))) for _ in range(9)]
empty = []
for i in range(9):
    for j in range(9):
        if grid[i][j] == 0:
            empty.append((i, j))

def dfs(i):
    if i == len(empty):
        for a in grid:
            print(''.join(map(str, a)))
        return True
    
    x, y = empty[i][0], empty[i][1]
    total_number = set([num for num in range(1,10)])
    used = set(grid[x] + [grid[r][y] for r in range(9)] + [grid[r][c] for r in range(3*(x//3),3*(x//3)+3) for c in range(3*(y//3), 3*(y//3) +3)])
    for num in sorted(total_number - used):
        grid[x][y] = num
        if dfs(i + 1):
            return True
        grid[x][y] = 0
    return False
        
dfs(0)